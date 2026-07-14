// Last updated: 14/07/2026, 14:56:38
class Solution {
    public int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
    return(arrivalTime+delayedTime) %24;   
    }
}