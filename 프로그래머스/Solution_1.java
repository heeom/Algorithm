package programmer;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

//https://programmers.co.kr/learn/courses/30/lessons/42576?language=java
class Solution_1 {
    public String solution(String[] participant, String[] completion) {

        Arrays.sort(participant);
        Arrays.sort(completion);

        int i=0;
        for(i=0; i<completion.length; i++){
            if(!participant[i].equals(completion[i])){
                break;
            }
        }
        return participant[i];
    }
}
//HashMap을 이용한 풀이
class Solution_2{
    public String solution(String[] participant, String[] completion){
        String answer = "";

        HashMap<String, Integer> map = new HashMap<>();
        for(String player : participant){
            map.put(player, map.getOrDefault(player, 0) + 1);
        }
        //완주자 체크 : 완주하면 player key에 대한 value값이 0이 된다.
        for(String player : completion){
            map.put(player, map.get(player) - 1);
        }

        Iterator<Map.Entry<String, Integer>> iterator = map.entrySet().iterator();

        while(iterator.hasNext()){
            Map.Entry<String, Integer> entry = iterator.next();
            if(entry.getValue() != 0){
                answer = entry.getKey();
            }
        }
        return answer;
    }
}

// map.entrySet() : map의 key, value값이 모두 필요한 경우
// keySet(), valueSet() : key, vaule값 각각 필요한 경우
// map.entrySet().iterator() : Set객체 반환 받은 후 iterator 인터페이스 사용

