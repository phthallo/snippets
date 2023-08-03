const value = process.argv[2];
if (value == 0) {
    console.log('alive');
} else if (value == 1) {
    console.log('flowering');
} else if (value == 2) {
    console.log("shedding");
} else if (value >= 3) {
    console.log("other")
}