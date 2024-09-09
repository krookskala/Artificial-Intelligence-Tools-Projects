public class Node {
    char ch;
    int frequency;
    Node left, right;

    public Node(char data, int frequency) {
        this.ch = data;
        this.frequency = frequency;
        left = right = null;
    }
}
