function task(x) {
    return typeof x === typeof null ? 'artmagedon' : x === 0 ? 1 : x * task(x-1);
}
