import lms

def test_lms():
    print("Starting tests...")

    # Test 1: Initial 5 students
    print(f"Initial student count: {len(lms.students)}")
    assert len(lms.students) == 5, f"Expected 5 students, got {len(lms.students)}"

    # Test 2: Add student
    lms.add_student("Test User", "test@example.com", "Test Father", "6th")
    print(f"Student count after add: {len(lms.students)}")
    assert len(lms.students) == 6, f"Expected 6 students, got {len(lms.students)}"

    # Test 3: Search student
    results = lms.search_student("Test User")
    print(f"Search results for 'Test User': {len(results)}")
    assert len(results) == 1, f"Expected 1 search result, got {len(results)}"
    assert results[0].name == "Test User"

    results_email = lms.search_student("alice@example.com")
    print(f"Search results for 'alice@example.com': {len(results_email)}")
    assert len(results_email) == 1
    assert results_email[0].name == "Alice Smith"

    # Test 4: Remove student
    lms.remove_student("test@example.com")
    print(f"Student count after remove: {len(lms.students)}")
    assert len(lms.students) == 5, f"Expected 5 students, got {len(lms.students)}"

    # Verify removal
    results_after = lms.search_student("test@example.com")
    assert len(results_after) == 0, "Student was not removed"

    print("All tests passed!")

if __name__ == "__main__":
    test_lms()
