/*Напишите функцию task(value), которая выполняет 
групповое кодирование строки: каждую последовательность 
одинаковых соседних символов заменяет этим символом и 
количеством его повторений.Например, строка aaabbccccd 
должна превратиться в a3b2c4d1.Функция должна возвращать 
объект с полями login и encoded, где login содержит ваш 
логин в этой системе, а encoded — закодированная строка.*/

function task(value) {
    let encoded = "";
    let count = 1;

    for (let i = 0; i < value.length; i++) {
        if (value[i] === value[i + 1]) {
            count++;
        } else {
            encoded += value[i] + count;
            count = 1;
        }
    }

    return {
        login: "artmagedon",
        encoded: encoded
    };
}