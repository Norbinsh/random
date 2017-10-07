// Receive a string, and return it in reversed order.
// Long way
function stringReverse(string_param)  {
  var turned_array = string_param.split('');
  var reversed_array = turned_array.reverse();
  var my_string = turned_array.join();
  return my_string.split(',').join('');
}

document.write(stringReverse("Your String Here"));

document.write("<br>");

// Receive a string, and return it in reversed order.
// Short way
function reverse(s) {
  return s.split('').reverse().join('');
}

// Test output
document.write(reverse("shay"));

// Break a line
document.write("<br>");


// Return the factorial number of a given positive integer
// For example, 5! = 1 * 2 * 3 * 4 * 5 = 120
// Using recursion, if num equals 0 we return the number 1, otherwise we keep calling our function while decrementing
// num by 1 each time.
function factorialize(num) {
    if (num === 0) {
        return 1;
    }

    return num * factorialize(num - 1);

    }

document.write(factorialize(5));


// Simple palindrome-or-not check, excluding all non alphabet character

function palindrome(str) {
  var clean_str = str.toLowerCase(str).replace(/[^a-zA-Z0-9]/g, '')
  var reversed_array = clean_str.split('').reverse().join('')
  if (clean_str === reversed_array) {
      return true;
  }
  return false;
}

//Find the Longest Word in a String

function findLongestWord(str) {
  var my_array = str.split(' ');
  var lowest_length = 0;
  my_array.forEach(function(elem) {
     if (elem.length > lowest_length) {
         lowest_length = elem.length;
     }});
  return lowest_length;
}

findLongestWord("The quick brown fox jumped over the lazy dog");


// Return the provided string with the first letter of each word capitalized. Make sure the rest of the word is in
// lower case.

function titleCase(str) {
  var splitArray = str.split(' ');
  tmpArray = [];
  for (var i=0; i<splitArray.length; i++) {
      tmpArray.push(splitArray[i][0].toUpperCase() + splitArray[i].slice(1, splitArray[i].length).toLowerCase());
  }
  return tmpArray.join(' ');
}

titleCase("sHoRt AnD sToUt") //should return "Short And Stout".


// Return an array consisting of the largest number from each provided sub-array.

function largestOfFour(arr) {
  arr.forEach(function(elem, elemindex) {
      arr[elemindex] = Math.max.apply(Math, elem);
  });
  return arr;
}

largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);


// Check if a string (first argument, str) ends with the given target string (second argument, target).


function confirmEnding(str, target) {
if (str.substr((str.length-target.length)) == target) {
return true;}
else {
return false;}
}


confirmEnding("Bastian", "n");


// Repeat a given string (first argument) num times (second argument). Return an empty string if num is not a positive
// number.

function repeatStringNumTimes(str, num) {
var myArray = [];
for (i=0; i<num; i++){
	myArray.push(str);
}
return myArray.join('');
}

repeatStringNumTimes("abc", 3);


// Truncate a string (first argument) if it is longer than the given maximum string length (second argument). Return the truncated string with a ... ending.
//
// Note that inserting the three dots to the end will add to the string length.
//
// However, if the given maximum string length num is less than or equal to 3, then the addition of the three dots does not add to the string length in determining the truncated string.

function truncateString(str, maxLength) {
 if ((str.length > maxLength) && (maxLength <= 3))    {
	return str.slice(0, maxLength) + "...";
 }
else if ((str.length > maxLength) && (maxLength > 3)) {
	return str.slice(0, maxLength-3) + "...";
}
  else {
    return str;
  }
 }

truncateString("A-tisket a-tasket A green and yellow basket", 11);

// Write a function that splits an array (first argument) into groups the length of size (second argument) and returns them as a two-dimensional array.


function chunkArrayInGroups(arr, size) {
  var tmpArray = [];
  var niceArray = [];
  while (arr.length > 0) {
    tmp_array = arr.splice(0,size);
    niceArray.push(tmp_array);
  }
  return niceArray;
}
chunkArrayInGroups(["a", "b", "c", "d"], 2);


// Return true if the string in the first element of the array contains all of the letters of the string in the second element of the array

function mutation(arr) {

  var firstPartArray = arr[0];
  var secondPartArray = arr.slice(1,2);

  for (var i=0; i<secondPartArray[0].length; i++) {

    if (firstPartArray.toLowerCase().indexOf(secondPartArray[0][i].toLowerCase()) === -1) {
      return false;
    }
  }
      return true;

}

mutation(["Mary", "Army"]);


// Remove all falsy values from an array.

function bouncer(arr) {
  var badArray = [false, null, 0, "", undefined, NaN]; // array with the bad values we want to exclude
  return arr.filter(function(v) { // using filter function
    return !badArray.includes(v); // returning the filtered array while negating items that are in the bad array
  });
}

bouncer([7, "ate", "", false, 9]);


// check if the function arguments, other than the array itself (index [0]) exist in the array, remove if so
function destroyer(arr) {
    var args = Array.prototype.slice.call(arguments).splice(1);
    return arr.filter(function(v) {
        return !args.includes(v);
    });
}

destroyer([1, 2, 3, 1, 2, 3], 2, 3);


// Return the lowest index at which a value (second argument) should be inserted into an array (first argument) once it has been sorted. The returned value should be a number.

function sortArray(arrToSort) {
    return arrToSort.sort(function(a,b) {return a-b;});
}

function getIndexToIns(arr, num) {
    var sortedArray = sortArray(arr);
    var indexPos = arr.indexOf(num);
    if (indexPos != -1) {
        return (indexPos);
    }
    else {
        for (var i=0; i<sortedArray.length; i++) {
            if (num < sortedArray[0]) {
                return 0;
            }
            else if (num > sortedArray[sortedArray.length -1]) {
                return (sortedArray.length);
            }
            if (num > sortedArray[i] && num < sortedArray[i+1]) {
                return i+1;
            }
        }
    }
}


// ROT13

function letterOrNot(letter) {
    return letter.length === 1 && letter.match(/[A-Z]/);
}

function rot13(str) {
    let strArray = [];
    let currentCode;
    for (let i=0; i<str.length; i++) {
        if (letterOrNot(str[i])) {
        currentCode = str[i].charCodeAt(0);
        if (currentCode < 78) {
            currentCode += 26;
        }
        strArray.push(String.fromCharCode(currentCode-13));

        }
        else {
            strArray.push(str[i]);
        }
    }
    console.log(strArray.join(''));
    return strArray.join('');
}

rot13("SERR PBQR PNZC");


// Array sum including 'withins'

function sumAll(givenArray)
	{
		const minNum = Math.min(...givenArray);
		const maxNum = Math.max(...givenArray);
		const edgesSum = minNum + maxNum;
		let tmpArray = [];
		let k = maxNum -1;

		while (k > minNum && k < maxNum) {
			tmpArray.push(k);
			k =  k - 1;
}
const tmpSum =  tmpArray.reduce( (a,b) => a+b );
return (edgesSum + tmpSum);
	}

sumAll([1,4]);

function diffArray(arr1, arr2) {
    var newArr = [];
    for (var i in arr1) {
        if (arr2.indexOf(arr1[i]) != -1) {
            newArr.push(arr1[i]);
        }
    }
    console.log(newArr);
}

diffArray([7,8,6,9,0],[1,8,6,1]);


