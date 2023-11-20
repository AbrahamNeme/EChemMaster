import React, { useEffect } from 'react';
import './styles.css';

function PeriodicTable() {
  useEffect(() => {
 const table_1 =  document.querySelector('.table-1')
    const table_2 =  document.querySelector('.table-2')

    function GENERATE_GRIDS(amount, className, table){
        for(let i = 0; i < amount; i++){
            let element = document.createElement('div')
            element.className = className
            table.appendChild(element)
        }
    }
    //let elements = document.querySelectorAll('element')

    GENERATE_GRIDS(90, 'element element_one',table_1)
    GENERATE_GRIDS(30, 'element element_two',table_2)

    let elements = document.querySelectorAll('.element_one, .element_two');

    elements.forEach(element => {
        element.onclick = () => {
            const elementSymbol = element.querySelector('.symbol').innerText;
            window.location.href = 'element.html?element=' + elementSymbol;
        };
    });

    const periodicTable = [
        { mass: 1.008, "element-name": "Hydrogen", category: "Nonmetal", symbol: "H" },
        { mass: 4.0026, "element-name": "Helium", category: "Noble Gas", symbol: "He" },
        { mass: 6.94, "element-name": "Lithium", category: "Alkali Metal", symbol: "Li" },
        { mass: 9.0122, "element-name": "Beryllium", category: "Alkaline Earth Metal", symbol: "Be" },
        { mass: 10.81, "element-name": "Boron", category: "Metalloid", symbol: "B" },
        { mass: 12.011, "element-name": "Carbon", category: "Nonmetal", symbol: "C" },
        { mass: 14.007, "element-name": "Nitrogen", category: "Nonmetal", symbol: "N" },
        { mass: 15.999, "element-name": "Oxygen", category: "Nonmetal", symbol: "O" },
        { mass: 18.998, "element-name": "Fluorine", category: "Nonmetal", symbol: "F" },
        { mass: 20.18, "element-name": "Neon", category: "Noble Gas", symbol: "Ne" },
        { mass: 22.99, "element-name": "Sodium", category: "Alkali Metal", symbol: "Na" },
        { mass: 24.305, "element-name": "Magnesium", category: "Alkaline Earth Metal", symbol: "Mg" },
        { mass: 26.982, "element-name": "Aluminum", category: "Other Metal", symbol: "Al" },
        { mass: 28.085, "element-name": "Silicon", category: "Metalloid", symbol: "Si" },
        { mass: 30.974, "element-name": "Phosphorus", category: "Nonmetal", symbol: "P" },
        { mass: 32.06, "element-name": "Sulfur", category: "Nonmetal", symbol: "S" },
        { mass: 35.45, "element-name": "Chlorine", category: "Nonmetal", symbol: "Cl" },
        { mass: 39.95, "element-name": "Argon", category: "Noble Gas", symbol: "Ar" },
        { mass: 39.10, "element-name": "Potassium", category: "Alkali Metal", symbol: "K" },
        { mass: 40.08, "element-name": "Calcium", category: "Alkaline Earth Metal", symbol: "Ca" },
        { mass: 44.96, "element-name": "Scandium", category: "Transition Metal", symbol: "Sc" },
        { mass: 47.87, "element-name": "Titanium", category: "Transition Metal", symbol: "Ti" },
        { mass: 50.94, "element-name": "Vanadium", category: "Transition Metal", symbol: "V" },
        { mass: 51.99, "element-name": "Chromium", category: "Transition Metal", symbol: "Cr" },
        { mass: 54.94, "element-name": "Manganese", category: "Transition Metal", symbol: "Mn" },
        { mass: 55.85, "element-name": "Iron", category: "Transition Metal", symbol: "Fe" },
        { mass: 58.93, "element-name": "Cobalt", category: "Transition Metal", symbol: "Co" },
        { mass: 58.69, "element-name": "Nickel", category: "Transition Metal", symbol: "Ni" },
        { mass: 63.55, "element-name": "Copper", category: "Transition Metal", symbol: "Cu" },
        { mass: 65.38, "element-name": "Zinc", category: "Transition Metal", symbol: "Zn" },
        { mass: 69.72, "element-name": "Gallium", category: "Other Metal", symbol: "Ga" },
        { mass: 72.63, "element-name": "Germanium", category: "Metalloid", symbol: "Ge" },
        { mass: 74.92, "element-name": "Arsenic", category: "Metalloid", symbol: "As" },
        { mass: 78.96, "element-name": "Selenium", category: "Nonmetal", symbol: "Se" },
        { mass: 79.90, "element-name": "Bromine", category: "Nonmetal", symbol: "Br" },
        { mass: 83.80, "element-name": "Krypton", category: "Noble Gas", symbol: "Kr" },
        { mass: 85.47, "element-name": "Rubidium", category: "Alkali Metal", symbol: "Rb" },
        { mass: 87.62, "element-name": "Strontium", category: "Alkaline Earth Metal", symbol: "Sr" },
        { mass: 88.91, "element-name": "Yttrium", category: "Transition Metal", symbol: "Y" },
        { mass: 91.22, "element-name": "Zirconium", category: "Transition Metal", symbol: "Zr" },
        { mass: 92.91, "element-name": "Niobium", category: "Transition Metal", symbol: "Nb" },
        { mass: 95.94, "element-name": "Molybdenum", category: "Transition Metal", symbol: "Mo" },
        { mass: 98.00, "element-name": "Technetium", category: "Transition Metal", symbol: "Tc" },
        { mass: 101.1, "element-name": "Ruthenium", category: "Transition Metal", symbol: "Ru" },
        { mass: 102.9, "element-name": "Rhodium", category: "Transition Metal", symbol: "Rh" },
        { mass: 106.4, "element-name": "Palladium", category: "Transition Metal", symbol: "Pd" },
        { mass: 107.9, "element-name": "Silver", category: "Transition Metal", symbol: "Ag" },
        { mass: 112.4, "element-name": "Cadmium", category: "Transition Metal", symbol: "Cd" },
        { mass: 114.8, "element-name": "Indium", category: "Other Metal", symbol: "In" },
        { mass: 118.7, "element-name": "Tin", category: "Other Metal", symbol: "Sn" },
        { mass: 121.8, "element-name": "Antimony", category: "Metalloid", symbol: "Sb" },
        { mass: 127.6, "element-name": "Tellurium", category: "Metalloid", symbol: "Te" },
        { mass: 126.9, "element-name": "Iodine", category: "Nonmetal", symbol: "I" },
        { mass: 131.3, "element-name": "Xenon", category: "Noble Gas", symbol: "Xe" },
        { mass: 132.9, "element-name": "Cesium", category: "Alkali Metal", symbol: "Cs" },
        { mass: 137.3, "element-name": "Barium", category: "Alkaline Earth Metal", symbol: "Ba" },
        { mass: 138.9, "element-name": "Lanthanum", category: "Lanthanide", symbol: "La" },
        { mass: 140.1, "element-name": "Cerium", category: "Lanthanide", symbol: "Ce" },
        { mass: 140.9, "element-name": "Praseodymium", category: "Lanthanide", symbol: "Pr" },
        { mass: 144.2, "element-name": "Neodymium", category: "Lanthanide", symbol: "Nd" },
        { mass: 145.0, "element-name": "Promethium", category: "Lanthanide", symbol: "Pm" },
        { mass: 150.4, "element-name": "Samarium", category: "Lanthanide", symbol: "Sm" },
        { mass: 152.0, "element-name": "Europium", category: "Lanthanide", symbol: "Eu" },
        { mass: 157.3, "element-name": "Gadolinium", category: "Lanthanide", symbol: "Gd" },
        { mass: 158.9, "element-name": "Terbium", category: "Lanthanide", symbol: "Tb" },
        { mass: 162.5, "element-name": "Dysprosium", category: "Lanthanide", symbol: "Dy" },
        { mass: 164.9, "element-name": "Holmium", category: "Lanthanide", symbol: "Ho" },
        { mass: 167.3, "element-name": "Erbium", category: "Lanthanide", symbol: "Er" },
        { mass: 168.9, "element-name": "Thulium", category: "Lanthanide", symbol: "Tm" },
        { mass: 173.0, "element-name": "Ytterbium", category: "Lanthanide", symbol: "Yb" },
        { mass: 175.0, "element-name": "Lutetium", category: "Lanthanide", symbol: "Lu" },
        { mass: 178.5, "element-name": "Hafnium", category: "Transition Metal", symbol: "Hf" },
        { mass: 180.9, "element-name": "Tantalum", category: "Transition Metal", symbol: "Ta" },
        { mass: 183.8, "element-name": "Tungsten", category: "Transition Metal", symbol: "W" },
        { mass: 186.2, "element-name": "Rhenium", category: "Transition Metal", symbol: "Re" },
        { mass: 190.2, "element-name": "Osmium", category: "Transition Metal", symbol: "Os" },
        { mass: 192.2, "element-name": "Iridium", category: "Transition Metal", symbol: "Ir" },
        { mass: 195.1, "element-name": "Platinum", category: "Transition Metal", symbol: "Pt" },
        { mass: 197.0, "element-name": "Gold", category: "Transition Metal", symbol: "Au" },
        { mass: 200.6, "element-name": "Mercury", category: "Transition Metal", symbol: "Hg" },
        { mass: 204.4, "element-name": "Thallium", category: "Other Metal", symbol: "Tl" },
        { mass: 207.2, "element-name": "Lead", category: "Other Metal", symbol: "Pb" },
        { mass: 208.9, "element-name": "Bismuth", category: "Other Metal", symbol: "Bi" },
        { mass: 209.0, "element-name": "Polonium", category: "Metalloid", symbol: "Po" },
        { mass: 210.0, "element-name": "Astatine", category: "Metalloid", symbol: "At" },
        { mass: 222.0, "element-name": "Radon", category: "Noble Gas", symbol: "Rn" },
        { mass: 223.0, "element-name": "Francium", category: "Alkali Metal", symbol: "Fr" },
        { mass: 226.0, "element-name": "Radium", category: "Alkaline Earth Metal", symbol: "Ra" },
        { mass: 227.0, "element-name": "Actinium", category: "Actinide", symbol: "Ac" },
        { mass: 232.0, "element-name": "Thorium", category: "Actinide", symbol: "Th" },
        { mass: 231.0, "element-name": "Protactinium", category: "Actinide", symbol: "Pa" },
        { mass: 238.0, "element-name": "Uranium", category: "Actinide", symbol: "U" },
        { mass: 237.0, "element-name": "Neptunium", category: "Actinide", symbol: "Np" },
        { mass: 244.0, "element-name": "Plutonium", category: "Actinide", symbol: "Pu" },
        { mass: 243.0, "element-name": "Americium", category: "Actinide", symbol: "Am" },
        { mass: 247.0, "element-name": "Curium", category: "Actinide", symbol: "Cm" },
        { mass: 247.0, "element-name": "Berkelium", category: "Actinide", symbol: "Bk" },
        { mass: 251.0, "element-name": "Californium", category: "Actinide", symbol: "Cf" },
        { mass: 252.0, "element-name": "Einsteinium", category: "Actinide", symbol: "Es" },
        { mass: 257.0, "element-name": "Fermium", category: "Actinide", symbol: "Fm" },
        { mass: 258.0, "element-name": "Mendelevium", category: "Actinide", symbol: "Md" },
        { mass: 259.0, "element-name": "Nobelium", category: "Actinide", symbol: "No" },
        { mass: 262.0, "element-name": "Lawrencium", category: "Actinide", symbol: "Lr" },
        { mass: 267.0, "element-name": "Rutherfordium", category: "Transition Metal", symbol: "Rf" },
        { mass: 270.0, "element-name": "Dubnium", category: "Transition Metal", symbol: "Db" },
        { mass: 271.0, "element-name": "Seaborgium", category: "Transition Metal", symbol: "Sg" },
        { mass: 270.0, "element-name": "Bohrium", category: "Transition Metal", symbol: "Bh" },
        { mass: 278.0, "element-name": "Hassium", category: "Transition Metal", symbol: "Hs" },
        { mass: 281.0, "element-name": "Meitnerium", category: "Transition Metal", symbol: "Mt" },
        { mass: 281.0, "element-name": "Darmstadtium", category: "Transition Metal", symbol: "Ds" },
        { mass: 285.0, "element-name": "Roentgenium", category: "Transition Metal", symbol: "Rg" },
        { mass: 285.0, "element-name": "Copernicium", category: "Transition Metal", symbol: "Cn" },
        { mass: 289.0, "element-name": "Nihonium", category: "Unknown", symbol: "Nh" },
        { mass: 293.0, "element-name": "Flerovium", category: "Unknown", symbol: "Fl" },
        { mass: 294.0, "element-name": "Moscovium", category: "Unknown", symbol: "Mc" },
        { mass: 294.0, "element-name": "Livermorium", category: "Unknown", symbol: "Lv" },
        { mass: 295.0, "element-name": "Tennessine", category: "Unknown", symbol: "Ts" },
        { mass: 294.0, "element-name": "Oganesson", category: "Noble Gas", symbol: "Og" }
    ]

    const element_1 = document.querySelectorAll('.element_one')
    const element_2 = document.querySelectorAll('.element_two')

    function display(min, max, table, offset = 0) {
        for (let i = min; i < max; i++) {
            let idx = i + offset;
            let atomic_number = idx + 1;
            let base = periodicTable[idx];
            table[i].innerHTML = `<span class='symbol'>${base.symbol}</span>`;
           /* table[i].innerHTML = `
            <span class='atomic_number'>${atomic_number}</span>
            <span class='mass'>${base.mass}</span>
            <span class='symbol'>${base.symbol}</span>
            <span class='name'>${base['element-name']}</span>
        `;*/

        }
    }

    display(0,56,element_1)
    display(57,74,element_1,14)
    display(75,90,element_1,28)
    display(0,15,element_2,56)
    display(15,30,element_2,73)

  //  element_1[56].innerHTML = '57-71 <span class = "bold">Lanthanides</span>'
    element_1[56].innerHTML = '<span class = "bold">Lanthanide</span>'
    element_1[56].classList.add('Lanthanide')

   // element_1[74].innerHTML = '89-103 <span class = "bold">Actinide</span>'
    element_1[74].innerHTML = '<span class = "bold">Actinide</span>'
    element_1[74].classList.add('Actinide')

    let exceptions = [element_1[56], element_1[74]]

    exceptions.forEach(item => {
        let base = item.style
        base.textAlign = 'center'
        base.display = 'flex'
        base.justifyContent = 'center'
        base.alignItems = 'center'
    })

    function color_code(min, max, table, offset = 0){

        for(let i = min; i < max; i++){
            let curr = table[i]
            let idx = i+offset
            let category = periodicTable[idx].category

            switch (category){
                case "Nonmetal":
                    curr.classList.add('Nonmetal')
                    break;
                case "Noble gas":
                    curr.classList.add('Noble-gas')
                    break;
                case "Alkali metal":
                    curr.classList.add('Alkali-metal')
                    break;
                case "Alkaline earth metal":
                    curr.classList.add('Alkaline-earth-metal')
                    break;
                case "Metalloid":
                    curr.classList.add('Metalloid')
                    break;
                case "Halogen":
                    curr.classList.add('Halogen')
                    break;
                case "Post-transition metal":
                    curr.classList.add('Post-transition-metal')
                    break;
                case "Transition metal":
                    curr.classList.add('Transition-metal')
                    break;
                case "Lanthanide":
                    curr.classList.add('Lanthanide')
                    break;
                case "Actinide":
                    curr.classList.add('Actinide')
                    break;
                case "Unknown":
                    curr.classList.add('Unknown')
                    break;
            }
        }
    }

    color_code(0,56,element_1)
    color_code(57,74,element_1,14)
    color_code(75,90,element_1,28)

    for (let i = 0; i < 15; i++){
        element_2[i].classList.add('Lanthanide')
    }
    for (let i = 15; i < 30; i++){
        element_2[i].classList.add('Actinide')
    }
  }, []);

  return (
  <div>
    <div className="table-1" style={{ display: 'grid', position: 'absolute', left: '50%', transform: 'translate(-50%, -50%)', gridTemplateColumns: 'repeat(18, 1fr)', top: '37.5%' }}>
    </div>
    <div className="table-2" style={{ display: 'grid', position: 'absolute', left: '50%', transform: 'translate(-50%, -50%)', gridTemplateColumns: 'repeat(14, 1fr)', top: '85%' }}>
    </div>
  </div>
  );
}

export default PeriodicTable;
