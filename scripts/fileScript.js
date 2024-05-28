import xlsx from "node-xlsx";
export const getData = (file) => {
    const workSheetsFromFile = xlsx.parse(file);

  const sheetNames = workSheetsFromFile[0].data[0].map((nombre) =>
    nombre.replace(/ /g, "_")
  );

  const jsonResultado = workSheetsFromFile[0].data.slice(1).map((valores) => {
    let objeto = {};
    sheetNames.forEach((nombre, i) => {
      objeto[nombre] = valores[i];
    });
    return objeto;
  });

  return jsonResultado.filter((person) => person.TELEFONO !== undefined);
};

console.log(getData());
