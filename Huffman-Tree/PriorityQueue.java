import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PriorityQueue {
    protected List<Node> heap;
    public PriorityQueue() {
        heap = new ArrayList<>();
    }

    public void add(Node node) {
        heap.add(node);
        int index = heap.size() - 1;
        while (index > 0) {
            int parentIndex = (index - 1) / 2;
            if (heap.get(index).frequency < heap.get(parentIndex).frequency) {
                Collections.swap(heap, index, parentIndex);
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    public Node check() {
        if (isEmpty()) return null;
        Node min = heap.get(0);
        heap.set(0, heap.get(heap.size() - 1));
        heap.remove(heap.size() - 1);
        int index = 0;
        while (true) {
            int leftChild = (2 * index) + 1;
            int rightChild = (2 * index) + 2;
            if (leftChild >= heap.size()) break;
            int smaller = leftChild;
            if (rightChild < heap.size() && heap.get(rightChild).frequency < heap.get(leftChild).frequency) {
                smaller = rightChild;
            }
            if (heap.get(smaller).frequency < heap.get(index).frequency) {
                Collections.swap(heap, index, smaller);
                index = smaller;
            } else {
                break;
            }
        }
        return min;
    }

    public boolean isEmpty() {
        return heap.isEmpty();
    }
}
