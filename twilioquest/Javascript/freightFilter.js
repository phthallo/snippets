function scanAndFilter(freightItems, forbiddenString) {
    let filtereditems = freightItems.filter(item => item != forbiddenString);
    return filtereditems;
}