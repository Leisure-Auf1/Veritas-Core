#!/usr/bin/env python3
"""
Veritas-Core Quickstart — 5-minute getting started.

Shows: RuntimeEngine, hooks, state machine, basic agent execution.

Run: python examples/quickstart_agent.py
"""
from __future__ import annotations


def main():
    print("=" * 60)
    print("  Veritas-Core Quickstart")
    print("=" * 60)
    print()

    # ═══════════════════════════════════════════════════════
    # Step 1: Import
    # ═══════════════════════════════════════════════════════
    from veritas.sdk import RuntimeClient, TaskRequest

    print("1️⃣  Import SDK")
    print("   from veritas.sdk import RuntimeClient, TaskRequest")
    print()

    # ═══════════════════════════════════════════════════════
    # Step 2: Create client
    # ═══════════════════════════════════════════════════════
    client = RuntimeClient()

    print("2️⃣  Create RuntimeClient")
    print("   client = RuntimeClient()")
    print()

    # ═══════════════════════════════════════════════════════
    # Step 3: Submit task
    # ═══════════════════════════════════════════════════════
    request = TaskRequest(objective="analyze", agent="analyst")
    result = client.run(request)

    print("3️⃣  Submit task")
    print(f"   request = TaskRequest(objective='analyze', agent='analyst')")
    print(f"   result = client.run(request)")
    print()
    print(f"   Status: {result.status}")
    print(f"   Session ID: {result.session_id}")
    print(f"   Execution time: {result.execution_time_ms}ms")
    print()

    # ═══════════════════════════════════════════════════════
    # Step 4: Check sessions
    # ═══════════════════════════════════════════════════════
    sessions = client.sessions()
    print(f"4️⃣  Check sessions")
    print(f"   Total sessions: {len(sessions)}")
    print()

    # ═══════════════════════════════════════════════════════
    # Done
    # ═══════════════════════════════════════════════════════
    print("=" * 60)
    print("  ✅ Quickstart Complete")
    print()
    print("  Next steps:")
    print("    • Try veritas.cli.main:main() for CLI")
    print("    • See runtime_demo.py for engine internals")
    print("    • See memory_demo.py for persistent storage")
    print("=" * 60)


if __name__ == "__main__":
    main()
