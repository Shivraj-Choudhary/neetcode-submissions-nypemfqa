class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();
        for (String str: strs) {
            res.append(str.length()).append("#").append(str);
        }
        return res.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int j = i;
            while (str.charAt(j) != '#') {
                j++;
            }
            int length = Integer.parseInt(str.substring(i, j));
            j++;
            
            res.add(str.substring(j, j+length));
            i = j + length;
        }
        return res;
    }
}//5#hello5#world (14)
// i =0,
// j =1,
