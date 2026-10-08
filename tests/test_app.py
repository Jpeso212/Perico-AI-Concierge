import asyncio
import json
import unittest

from runtime.app import app


async def request(path, method="GET"):
    events = []

    async def receive():
        return {"type": "http.request", "body": b"", "more_body": False}

    async def send(message):
        events.append(message)

    await app({"type": "http", "method": method, "path": path}, receive, send)
    return events


class AppTests(unittest.TestCase):
    def test_health(self):
        events = asyncio.run(request("/health"))
        self.assertEqual(events[0]["status"], 200)
        self.assertEqual(json.loads(events[1]["body"]), {"status": "ok"})

    def test_no_booking_endpoints(self):
        for path in ("/bookings", "/payments", "/quotes", "/admin"):
            events = asyncio.run(request(path))
            self.assertEqual(events[0]["status"], 404)

    def test_health_is_read_only(self):
        events = asyncio.run(request("/health", "POST"))
        self.assertEqual(events[0]["status"], 405)

    def test_no_cache(self):
        events = asyncio.run(request("/health"))
        self.assertIn((b"cache-control", b"no-store"), events[0]["headers"])
