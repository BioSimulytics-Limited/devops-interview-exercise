"""A test script that hits the weather API's /predict endpoint with payloads of increasing size."""

import datetime
import json
import logging
import random
import time
import urllib.error
import urllib.request

logger = logging.getLogger(__name__)


def generate_readings(
    n: int, humidity_range: tuple[float, float] = (30.0, 100.0)
) -> list[dict]:
    """Generate `n` fake weather readings with a configurable humidity range."""
    base_time = datetime.datetime(2000, 1, 1, tzinfo=datetime.UTC)
    readings = []
    for i in range(n):
        readings.append(
            {
                "timestamp": (base_time + datetime.timedelta(hours=i)).isoformat()
                + "Z",
                "temperature": round(random.uniform(5.0, 35.0), 1),
                "humidity": round(random.uniform(*humidity_range), 1),
                "pressure": round(random.uniform(980.0, 1040.0), 2),
                "wind_speed": round(random.uniform(0.0, 60.0), 1),
            }
        )
    return readings


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s",
    )

    iteration = 0
    n = random.randint(5, 10)
    while True:
        h_low = random.uniform(30.0, 60.0)
        h_high = random.uniform(61.0, 100.0)

        logger.info(f"Iteration {iteration}: {n} readings")
        readings = generate_readings(n, humidity_range=(h_low, h_high))
        req = urllib.request.Request(
            "http://localhost:8080/predict",
            data=json.dumps({"readings": readings}).encode(),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                logger.info(f"Response status: {resp.status}")
                logger.info(
                    f"Response body: {json.dumps(json.loads(resp.read()), indent=4)}"
                )

        except urllib.error.URLError:
            logger.error("Connection error — server may have crashed!")
            break

        except TimeoutError:
            logger.error("Request timed out after 15 s")

        except Exception as exc:  # noqa: BLE001
            logger.error(f"Unexpected error: {exc}")

        time.sleep(random.uniform(0.5, 1.5))
        iteration += 1
        n *= 2
