public int ladderLength(String beginWord, String endWord, List<String> wordList) {
    Set<String> wordSet = new HashSet<>(wordList);
    if (!wordSet.contains(endWord)) return 0;
    Queue<String> queue = new LinkedList<>();
    queue.add(beginWord);
    int length = 1;
    while (!queue.isEmpty()) {
        int size = queue.size();
        for (int i = 0; i < size; i++) {
            String word = queue.poll();
            if (word.equals(endWord)) return length;
            char[] wordArray = word.toCharArray();
            for (int j = 0; j < wordArray.length; j++) {
                char originalChar = wordArray[j];
                for (char c = 'a'; c <= 'z'; c++) {
                    wordArray[j] = c;
                    String newWord = new String(wordArray);
                    if (wordSet.contains(newWord)) {
                        queue.add(newWord);
                        wordSet.remove(newWord);
                    }
                }
                wordArray[j] = originalChar;
            }
        }
        length++;
    }
    return 0;
}
