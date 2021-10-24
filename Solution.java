/* Magic Square and minimum cost function

    You will be given a 3x3 matrix s of integers in the inclusive range [1,9]. 
    We can convert any digit a to any other digit b in the range [1,9] at cost of |a-b|. 
    Given s, convert it into a magic square at minimal cost. Print this cost on a new line.
    Note: The resulting magic square must contain distinct integers in the inclusive range [1,9].

    My Notes: every 3x3 magic square must have a 5 in the middle, and each number must be unique in the end.
    Thus, the sum of any row or col/diag must be exactly 15 for a 3x3.
    The standard magic square looks something like:
    8 1 6
    3 5 7
    4 9 2

    All possible 3x3 magic square are listed below:
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
*/
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'formingMagicSquare' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY s as parameter.
     */

    public static int formingMagicSquare(List<List<Integer>> s) {
        // Write your code here
        if (is3x3MagicSquare(s)) { // already a magic square 3x3
            return 0; 
        }

        int[][][] allPossibleMagic3Squares = { // compare against magic squares
            {{8, 1, 6}, {3, 5, 7}, {4, 9, 2}},
            {{6, 1, 8}, {7, 5, 3}, {2, 9, 4}},
            {{4, 9, 2}, {3, 5, 7}, {8, 1, 6}},
            {{2, 9, 4}, {7, 5, 3}, {6, 1, 8}}, 
            {{8, 3, 4}, {1, 5, 9}, {6, 7, 2}},
            {{4, 3, 8}, {9, 5, 1}, {2, 7, 6}}, 
            {{6, 7, 2}, {1, 5, 9}, {8, 3, 4}},
            {{2, 7, 6}, {9, 5, 1}, {4, 3, 8}}
        };

        ArrayList<Integer> potentialCosts = new ArrayList<>();
        // go through each row of each predefined 3x3 matrix and compare with given matrix
        for (int[][] square : allPossibleMagic3Squares) {
            int currentTotal = 0;
            for (int row = 0; row < s.size(); row++) {
                for (int col = 0; col < s.size(); col++) {
                    currentTotal += Math.abs(s.get(row).get(col) - square[row][col]);
                }
            }
            potentialCosts.add(currentTotal);
        }

        return Collections.min(potentialCosts);
    }
    
    // Returns true if the given 2D List is a Magic Square.
    public static boolean is3x3MagicSquare(List<List<Integer>> s) {
        int magicSum = 15;
        int diagLeftSum = 0;
        int diagRightSum = 0;
        int diagLeftPosition = 0;
        int diagRightPosition = s.size() - 1;

        // 3x3 must have a 5 in middle
        int middle = s.size()/2;
        if (s.get(middle).get(middle) != 5) { return false; }
        
        // summing rows
        int currSum = 0;
        for (int row = 0; row < s.size(); row++, currSum = 0) {
            for (int col = 0; col < s.size(); col++) {
                currSum += s.get(row).get(col);
            }
            if (currSum != magicSum) { return false; }
        }
        
        // summing cols
        currSum = 0;
        for (int col = 0; col < s.size(); col++, currSum = 0) {
            for (int row = 0; row < s.size(); row++) {
                currSum += s.get(row).get(col);
            }
            if (currSum != magicSum) { return false; }
        }
        
        // summing diagonals
        for (int row = 0; row < s.size(); row++) {
            diagLeftSum += s.get(row).get(diagLeftPosition);
            diagRightSum += s.get(row).get(diagRightPosition);
            diagLeftPosition += 1;
            diagRightPosition -= 1;
        }
        
        return (diagRightSum == magicSum && diagLeftSum == magicSum);
    }

    public static void plusMinus(List<Integer> arr) {
        // Write your code here
        double size = arr.size();
        double pos = 0;
        double neg = 0;
        double zero = 0;
        for (int num : arr) {
            if (num > 0) {
                pos++;
            } else if (num == 0) {
                zero++;
            } else {
                neg++;
            }
        }
        
        double decimalPlace = 1000000.0;
        String positiveFormat = "" + Math.round(pos / size * decimalPlace) / decimalPlace;
        String negativeFormat = "" + Math.round(neg / size * decimalPlace) / decimalPlace;
        String zeroFormat = "" + Math.round(zero / size * decimalPlace) / decimalPlace;
        while (positiveFormat.length() < 8) {
            positiveFormat += "0";
        }
        while (negativeFormat.length() < 8) {
            negativeFormat += "0";
        } 
        while (zeroFormat.length() < 8) {
            zeroFormat += "0";
        }
        System.out.println(positiveFormat);
        System.out.println(negativeFormat);
        System.out.println(zeroFormat);
    }

}

// Not part of my solution
public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        List<List<Integer>> s = new ArrayList<>();

        IntStream.range(0, 3).forEach(i -> {
            try {
                s.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        int result = Result.formingMagicSquare(s);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
