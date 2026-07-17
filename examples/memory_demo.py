#!/usr/bin/env python3
"""
Veritas-Core Memory Demo — Student memory, mastery tracking, learning summary.

Shows: MemoryManager, StudentMemory, experience storage.

Run: python examples/memory_demo.py
"""
from __future__ import annotations


def main():
    print("=" * 60)
    print("  Veritas-Core Memory Demo")
    print("=" * 60)
    print()

    from veritas.memory import MemoryManager

    mm = MemoryManager()
    student_id = "demo_student_001"

    memory = mm.get_student_memory(student_id)
    print(f"1️⃣  Student: {student_id}")
    print(f"   Feedback items: {len(memory.feedback_history)}")
    print(f"   Weak points: {len(memory.weak_points)}")
    print()

    profile = {"knowledge_base": "beginner", "cognitive_style": "visual_dominant"}
    mm.update_student_memory(
        student_id, profile=profile,
        mastery_updates={"python_basics": 0.8, "python_oop": 0.6, "python_decorators": 0.3},
    )

    print("2️⃣  Mastery Map:")
    memory_after = mm.get_student_memory(student_id)
    mastery = getattr(memory_after, 'mastery_map', {})
    for concept, score in sorted(mastery.items()):
        bar = "█" * int(score * 10) + "░" * (10 - int(score * 10))
        emoji = "🟢" if score >= 0.8 else "🟡" if score >= 0.5 else "🔴"
        print(f"   {emoji} {concept}: {bar} {score:.0%}")
    print()

    mm.store_experience(
        problem="Confused @decorator syntax",
        cause="Unfamiliar with higher-order functions",
        context="python_decorators",
        solution="Practice writing simple decorators step by step",
    )
    print("3️⃣  Experience stored")
    stats = mm.get_experience_stats()
    print(f"   Total experiences: {stats.get('total', 0)}")
    print()

    summary = mm.get_learning_summary(student_id)
    print("4️⃣  Learning Summary:")
    for key, value in summary.items():
        print(f"   {key}: {value}")
    print()

    print("=" * 60)
    print("  ✅ Memory Demo Complete")
    print("=" * 60)


if __name__ == "__main__":
    main()
