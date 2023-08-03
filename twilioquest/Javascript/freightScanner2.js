function scan(freightItems) {
    let contrabandIndexes = [];

    freightItems.forEach((item, index) => {
        if (item == "contraband"){
            contrabandIndexes.push(index);
        } 
    })
    return contrabandIndexes;

}  