    public String ans(String[] strs) {
        
        String c = "";
        int lenSmallestWord = Integer.MAX_VALUE;
        
        for (String word: strs){
            lenSmallestWord = Math.min(lenSmallestWord, word.length());
        }
        
        for (int i = 0; i < lenSmallestWord; i++) {
            String first = strs[0];
            char letter = first.charAt(i);
            
            for (String word: strs) {
                if (word.charAt(i) != letter) {
                    return first.substring(0, i);
                }
            }
            
            c += letter;
        }
        
        return c;
    }
