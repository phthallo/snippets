function calculateMass(array){
    let totalMass = array.reduce((sum, item) => sum + item.length, 0)
    return totalMass;
}