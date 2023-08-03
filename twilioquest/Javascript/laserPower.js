function calculatePower(array){
    let totalPower = array.reduce((sum, item) => sum + (item * 2), 0);
    return totalPower;
}