const firstValue = (process.argv[2]).toLowerCase();
const secondValue = (process.argv[3]).toLowerCase();

// Your comparison code (if statements) go here
if (firstValue < secondValue){
    console.log(-1);
} else if (firstValue == secondValue){
    console.log(0);
} else if (firstValue > secondValue){
    console.log(1);
}