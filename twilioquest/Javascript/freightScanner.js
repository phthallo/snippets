function scan(array){
    let contrabandFound = 0; //do let instead of const, because const = constant and this value is going to be changed
    for (element of array) {
        if (element == "contraband"){
            contrabandFound +=1;
        }
    }
    return contrabandFound
}