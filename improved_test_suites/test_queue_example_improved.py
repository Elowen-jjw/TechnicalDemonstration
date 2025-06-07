import pytest
import array
import queue_example as module_0

def test_full_on_empty_queue():
    # Intent: Verify that a newly created queue is not full.
    
    # Arrange: Create a queue with a specified maximum size.
    size_max = 1256
    queue = module_0.Queue(size_max)

    # Act: Check if the queue is full.
    is_queue_full = queue.full()

    # Assert: Verify the initial state of the queue.
    assert queue.__dict__ == {
        "max": size_max,
        "head": 0,
        "tail": 0,
        "size": 0,
        "data": queue.data,
    }
    assert len(queue.data) == size_max

    # Assert: Verify that the queue is not full.
    assert is_queue_full is False

def test_initializeQueue_withInvalidSize_raisesAssertionError():
    # Intent: Verify that initializing a Queue with an invalid size raises an AssertionError.
    
    # Act and Assert: Expect an AssertionError when a Queue is initialized with a negative size.
    with pytest.raises(AssertionError):
        module_0.Queue(-2944)

def test_enqueue_negative_value():
    # Intent: Validate enqueue operation with a negative integer value

    # Arrange: Set up initial conditions
    negative_value = -726
    queue_capacity = 2505
    expected_tail_position = 1
    expected_queue_size = 1

    # Act: Create a queue and attempt to enqueue a negative value
    queue = module_0.Queue(queue_capacity)
    enqueue_result = queue.enqueue(negative_value)

    # Assert: Verify initial queue properties
    assert isinstance(queue, module_0.Queue)  # Check if queue is correctly instantiated
    assert queue.max == queue_capacity  # Ensure queue capacity is set correctly
    assert queue.head == 0  # Initial head position should be 0
    assert queue.tail == 0  # Initial tail position should be 0
    assert queue.size == 0  # Initial size should be 0
    assert isinstance(queue.data, array.array)  # Verify data storage type
    assert len(queue.data) == queue_capacity  # Ensure data array matches capacity

    # Assert: Verify enqueue operation results
    assert enqueue_result is True  # Enqueue should succeed
    assert queue.tail == expected_tail_position  # Tail should move to next position
    assert queue.size == expected_queue_size  # Size should reflect one item enqueued

    # Assert: Verify queue cannot be initialized with a negative size
    with pytest.raises(AssertionError):
        module_0.Queue(negative_value)  # Negative size should raise an assertion error

def test_dequeue_empty_queue():
    # Intent: Validate behavior of dequeue on an empty queue
    # Arrange
    size_max = 2423
    expected_queue_name = "queue_example.Queue"
    expected_array_name = "array.array"
    queue = module_0.Queue(size_max)

    # Act
    dequeued_value = queue.dequeue()

    # Assert: Verify queue type and initial state
    assert (
        f"{type(queue).__module__}.{type(queue).__qualname__}"
        == expected_queue_name
    )
    assert queue.__dict__ == {
        'max': size_max,
        'head': 0,
        'tail': 0,
        'size': 0,
        'data': queue.data
    }
    
    # Assert: Verify internal data structure type and size
    assert (
        f"{type(queue.data).__module__}.{type(queue.data).__qualname__}"
        == expected_array_name
    )
    assert len(queue.data) == size_max
    
    # Assert: Verify queue is not full and handle invalid queue creation
    assert queue.full() is False
    with pytest.raises(AssertionError):
        module_0.Queue(queue.full())

def test_enqueue_dequeue_operations():
    # Intent: Validate enqueue and dequeue operations on Queue

    # Arrange: Initialize queues with different sizes
    size_0 = 1001
    size_1 = 649
    size_2 = 3263
    value = 2010
    expected_class = "queue_example.Queue"
    expected_data_type = "array.array"

    queue_0 = module_0.Queue(size_0)
    queue_1 = module_0.Queue(size_1)
    queue_2 = module_0.Queue(size_2)

    # Act: Perform enqueue and dequeue operations
    enqueue_1 = queue_1.enqueue(value)
    dequeue_1 = queue_1.dequeue()
    enqueue_2 = queue_1.enqueue(value)

    # Assert: Verify queue_0 properties
    assert (
        f"{type(queue_0).__module__}.{type(queue_0).__qualname__}"
        == expected_class
    ), "Queue class type should match expected class"
    assert queue_0.max == size_0, "Queue max size should match initialized size"
    assert (
        f"{type(queue_0.data).__module__}.{type(queue_0.data).__qualname__}"
        == expected_data_type
    ), "Queue data type should be array.array"
    assert len(queue_0.data) == size_0, "Queue data length should match initialized size"

    # Assert: Verify initial state of queue_1
    assert queue_1.head == 0, "Initial head of queue_1 should be 0"
    assert queue_1.tail == 0, "Initial tail of queue_1 should be 0"
    assert queue_1.size == 0, "Initial size of queue_1 should be 0"

    # Assert: Verify initial state of queue_2
    assert queue_2.head == 0, "Initial head of queue_2 should be 0"
    assert queue_2.tail == 0, "Initial tail of queue_2 should be 0"
    assert queue_2.size == 0, "Initial size of queue_2 should be 0"
    assert queue_2.full() is False, "queue_2 should not be full initially"

    # Assert: Verify enqueue operation on queue_1
    assert enqueue_1 is True, "Enqueue operation should succeed"
    assert queue_1.tail == 1, "Tail should increment after enqueue"
    assert queue_1.size == 1, "Size should increment after enqueue"

    # Assert: Verify dequeue operation on queue_1
    assert dequeue_1 == value, "Dequeue should return the enqueued value"
    assert queue_1.head == 1, "Head should increment after dequeue"
    assert queue_1.size == 0, "Size should decrement after dequeue"

    # Assert: Verify queue fullness
    assert queue_0.full() is False, "queue_0 should not be full"
    assert queue_1.full() is False, "queue_1 should not be full after dequeue"

    # Assert: Verify second enqueue operation on queue_1
    assert enqueue_2 is True, "Second enqueue operation should succeed"
    assert queue_1.tail == 2, "Tail should increment after second enqueue"
    assert queue_1.size == 1, "Size should increment after second enqueue"

def test_initialize_queue_and_enqueue():
    # Intent: Validate queue initialization and enqueue operation

    # Arrange
    small_size = 1235
    large_size = 3504
    value_to_enqueue = 4904
    initial_index = 0

    # Act
    queue_a = module_0.Queue(small_size)
    queue_b = module_0.Queue(small_size)
    queue_c = module_0.Queue(large_size)
    is_empty_b = queue_b.empty()
    enqueue_result = queue_c.enqueue(value_to_enqueue)

    # Assert: Verify queue_a initialization
    assert (
        f"{type(queue_a).__module__}.{type(queue_a).__qualname__}"
        == "queue_example.Queue"
    )
    assert queue_a.max == small_size
    assert queue_a.head == initial_index
    assert queue_a.tail == initial_index
    assert queue_a.size == initial_index
    assert (
        f"{type(queue_a.data).__module__}.{type(queue_a.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_a.data) == small_size

    # Assert: Verify queue_b state and empty check
    assert queue_b.head == initial_index
    assert queue_b.tail == initial_index
    assert queue_b.size == initial_index
    assert is_empty_b is False

    # Assert: Verify queue_c state after enqueue operation
    assert queue_c.head == initial_index
    assert queue_c.tail == 1
    assert queue_c.size == 1
    assert enqueue_result is True

def test_enqueue_dequeue_operations():
    # Intent: Validate enqueue and dequeue operations on various queue sizes

    # Arrange
    size_1187 = 1187
    size_1 = 1
    size_1080 = 1080
    size_1441 = 1441
    size_2245 = 2245
    size_481 = 481

    # Create queues of different sizes
    queue_large = module_0.Queue(size_1187)
    queue_single_1 = module_0.Queue(size_1)
    queue_medium = module_0.Queue(size_1080)
    queue_single_2 = module_0.Queue(size_1)
    queue_single_3 = module_0.Queue(size_1)
    queue_small = module_0.Queue(size_481)

    # Act
    # Check if the large queue is initially empty
    is_large_empty = queue_large.empty()
    # Enqueue an element in the large queue
    enqueue_large = queue_large.enqueue(size_1187)
    # Check if the single-element queue is initially full
    is_single_1_full_initial = queue_single_1.full()
    # Enqueue an element in the single-element queue
    enqueue_single_1 = queue_single_1.enqueue(size_1441)
    # Check if the single-element queue is full after enqueue
    is_single_1_full_after_enqueue = queue_single_1.full()
    # Check if another single-element queue is initially empty
    is_single_2_empty_initial = queue_single_2.empty()
    # Check if the first single-element queue is empty after enqueue
    is_single_1_empty_after_enqueue = queue_single_1.empty()
    # Dequeue an element from the large queue
    dequeue_large = queue_large.dequeue()
    # Enqueue an element in the small queue using the full status of the single-element queue
    enqueue_small = queue_small.enqueue(is_single_1_full_after_enqueue)
    # Check if the large queue is empty after dequeue
    is_large_empty_after_dequeue = queue_large.empty()

    # Assert
    # Verify the initial state and type of the large queue
    assert (
        f"{type(queue_large).__module__}.{type(queue_large).__qualname__}"
        == "queue_example.Queue"
    )
    assert queue_large.max == size_1187
    assert queue_large.head == 0
    assert queue_large.tail == 0
    assert queue_large.size == 0
    assert (
        f"{type(queue_large.data).__module__}.{type(queue_large.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_large.data) == size_1187
    assert is_large_empty is False
    assert enqueue_large is True
    assert queue_large.tail == 1
    assert queue_large.size == 1

    # Verify the state and type of the first single-element queue after enqueue
    assert (
        f"{type(queue_single_1).__module__}.{type(queue_single_1).__qualname__}"
        == "queue_example.Queue"
    )
    assert queue_single_1.max == size_1
    assert (
        f"{type(queue_single_1.data).__module__}.{type(queue_single_1.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_single_1.data) == size_1
    assert is_single_1_full_initial is False
    assert enqueue_single_1 is True
    assert queue_single_1.size == 1
    assert is_single_1_full_after_enqueue is True

    # Verify the state and type of the second single-element queue
    assert (
        f"{type(queue_single_2).__module__}.{type(queue_single_2).__qualname__}"
        == "queue_example.Queue"
    )
    assert queue_single_2.max == size_1
    assert (
        f"{type(queue_single_2.data).__module__}.{type(queue_single_2.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_single_2.data) == size_1
    assert is_single_2_empty_initial is False
    assert is_single_1_empty_after_enqueue is True

    # Verify the state of the large queue after dequeue
    assert dequeue_large == size_1187
    assert queue_large.head == 1
    assert queue_large.size == 0

    # Verify the state of the small queue after enqueue
    assert enqueue_small is True
    assert queue_small.tail == 1
    assert queue_small.size == 1
    assert is_large_empty_after_dequeue is False

def test_enqueue_and_dequeue_operations():
    # Intent: Validate enqueue and dequeue operations on queues of different sizes

    # Arrange
    large_size = 1187
    single_size = 1
    medium_size = 1080
    large_value = 1187
    small_value = 1441
    invalid_size = -30

    large_queue = module_0.Queue(large_size)
    single_queue = module_0.Queue(single_size)
    medium_queue = module_0.Queue(medium_size)

    # Act
    large_empty = large_queue.empty()  # Check if a newly created large queue is empty
    large_enqueue = large_queue.enqueue(large_value)  # Enqueue a value to the large queue
    single_full_before = single_queue.full()  # Check if a newly created single queue is full
    single_enqueue = single_queue.enqueue(small_value)  # Enqueue a value to the single queue
    single_full_after = single_queue.full()  # Check if the single queue is full after enqueue
    single_dequeue = single_queue.dequeue()  # Dequeue from the single queue
    large_dequeue = large_queue.dequeue()  # Dequeue from the large queue
    medium_full = medium_queue.full()  # Check if a newly created medium queue is full
    single_enqueue_again = single_queue.enqueue(large_empty)  # Enqueue a boolean to the single queue

    # Assert
    # Verify large queue properties after operations
    assert isinstance(large_queue, module_0.Queue)
    assert large_queue.max == large_size
    assert large_queue.tail == 1
    assert large_queue.size == 1

    # Verify single queue properties before and after operations
    assert isinstance(single_queue, module_0.Queue)
    assert single_queue.max == single_size
    assert single_full_before is False
    assert single_enqueue is True
    assert single_queue.size == 1
    assert single_full_after is True

    # Verify medium queue remains empty
    assert medium_queue.size == 0

    # Verify dequeue operation on single queue
    assert single_dequeue == small_value
    assert single_queue.size == 0

    # Verify dequeue operation on large queue
    assert large_dequeue == large_value
    assert large_queue.head == 1
    assert large_queue.size == 0

    # Verify medium queue is not full and single queue can enqueue again
    assert medium_full is False
    assert single_enqueue_again is True
    assert single_queue.size == 1

    # Verify that creating a queue with invalid size raises an AssertionError
    with pytest.raises(AssertionError):
        module_0.Queue(invalid_size)