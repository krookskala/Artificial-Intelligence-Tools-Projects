import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Huffman {

    public static Node buildTree(Map<Character, Integer> freqMap) {
        PriorityQueue prque = new PriorityQueue();
        for (Map.Entry<Character, Integer> entry : freqMap.entrySet()) {
            prque.add(new Node(entry.getKey(), entry.getValue()));
        }
        while (prque.heap.size() > 1) {
            Node left = prque.check();
            Node right = prque.check();
            Node parent = new Node('\0', left.frequency + right.frequency);
            parent.left = left;
            parent.right = right;
            prque.add(parent);
        }
        return prque.check();
    }

    public static void generateCodes(Node root, String code, Map<Character, String> codes) {
        if (root == null) return;
        if (root.ch != '\0') {
            codes.put(root.ch, code);
        }
        generateCodes(root.left, code + "0", codes);
        generateCodes(root.right, code + "1", codes);
    }

    public static String encode(String input, Map<Character, String> codes) {
        StringBuilder sb = new StringBuilder();
        for (char c : input.toCharArray()) {
            sb.append(codes.get(c));
        }
        return sb.toString();
    }

    public static String decode(String encoded, Node root) {
        StringBuilder sb = new StringBuilder();
        Node current = root;
        for (char bit : encoded.toCharArray()) {
            if (bit == '0') {
                current = current.left;
            } else {
                current = current.right;
            }
            if (current.ch != '\0') {
                sb.append(current.ch);
                current = root;
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.print("Enter A String To Encode: ");
        String input = new Scanner(System.in).nextLine();
        Map<Character, Integer> freqMap = new HashMap<>();
        for (char c : input.toCharArray()) {
            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
        }

        Node root = buildTree(freqMap);
        Map<Character, String> codes = new HashMap<>();
        generateCodes(root, "", codes);

        System.out.println("Huffman Codes:");
        for (Map.Entry<Character, String> entry : codes.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }

        String encoded = encode(input, codes);
        System.out.println("Encoded: " + encoded);

        String decoded = decode(encoded, root);
        System.out.println("Decoded: " + decoded);
    }
}