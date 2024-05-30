import type DiseaseDatasheet from "../types/DiseaseDatasheet";

let arrayOfSheets : DiseaseDatasheet[] = [
  {
    name: "COVID-19",
    type: "Virus",
    cautions: {
      list: ["Wear a mask", "Wash your hands", "Avoid close contact"],
      info: ["Info 1"],
      files: ["File 1"]
    },
    cleaning: {
      list: ["Clean and disinfect frequently touched surfaces"],
      info: [],
      files: []
    },
    isolation: {
      isolationTime: 14,
      isolationPeriod: "days",
      info: ["Info 1"],
      files: ["File 1"]
    },
    mandatoryNotification: {
      notify: true,
      info: ["Info 1"],
      files: ["File 1"]
    },
    roomSharing: {
      shareable: false,
      info: ["Info 1"],
      files: ["File 1"]
    },
    warnings: ["COVID-19 is highly contagious", "COVID-19 can be deadly"]
  },
  {
    name: "Influenza",
    type: "Virus",
    cautions: {
      list: ["Wear a mask"],
      info: ["Info 1", "Info 2"],
      files: ["File 1", "File 2"]
    },
    cleaning: {
      list: ["Clean and disinfect frequently touched surfaces"],
      info: [],
      files: []
    },
    isolation: {
      isolationTime: 5,
      isolationPeriod: "days",
      info: ["Info 1"],
      files: []
    },
    mandatoryNotification: {
      notify: false,
      info: [],
      files: []
    },
    roomSharing: {
      shareable: true,
      info: [],
      files: ["File 1"]
    },
    warnings: []
  },
  {
    name: "Salmonella",
    type: "Bacteria",
    cautions: {
      list: ["Wash your hands", "Cook food thoroughly"],
      info: [],
      files: []
    },
    cleaning: {
      list: ["Clean and disinfect food preparation areas"],
      info: [],
      files: []
    },
    isolation: {
      isolationTime: 2,
      isolationPeriod: "weeks",
      info: ["Info 1"],
      files: ["File 1", "File 2"]
    },
    mandatoryNotification: {
      notify: true,
      info: [],
      files: []
    },
    roomSharing: {
      shareable: false,
      info: [],
      files: ["File 1"]
    },
    warnings: []
  },
  {
    name: "Tuberculosis",
    type: "Bacteria",
    cautions: {
      list: ["Wear a mask", "Wash your hands"],
      info: ["Info 1"],
      files: ["File 1"]
    },
    cleaning: {
      list: ["Clean and disinfect frequently touched surfaces"],
      info: [],
      files: []
    },
    isolation: {
      isolationTime: 14,
      isolationPeriod: "days",
      info: ["Info 1"],
      files: []
    },
    mandatoryNotification: {
      notify: false,
      info: ["Info 1"],
      files: []
    },
    roomSharing: {
      shareable: false,
      info: ["Info 1"],
      files: ["File 1"]
    },
    warnings: ["Tuberculosis is highly contagious"]
  },
  {
    name: "Staphylococcus",
    type: "Bacteria",
    cautions: {
      list: ["Wash your hands", "Avoid close contact", "Cover wounds"],
      info: [],
      files: []
    },
    cleaning: {
      list: ["Clean and disinfect wounds", "Clean and disinfect frequently touched surfaces"],
      info: [],
      files: []
    },
    isolation: {
      isolationTime: 1,
      isolationPeriod: "week",
      info: [],
      files: ["File 1"]
    },
    mandatoryNotification: {
      notify: true,
      info: ["Info 1"],
      files: []
    },
    roomSharing: {
      shareable: false,
      info: [],
      files: []
    },
    warnings: []
  },
  {
    name: "Hepatitis A",
    type: "Virus",
    cautions: {
      list: ["Wash your hands", "Avoid raw food", "Cook food thoroughly"],
      info: [],
      files: []
    },
    cleaning: {
      list: ["Clean and disinfect food preparation areas"],
      info: [],
      files: []
    },
    isolation: {
      isolationTime: 0,
      isolationPeriod: "Alta médica",
      info: [],
      files: []
    },
    mandatoryNotification: {
      notify: true,
      info: ["Info 1"],
      files: ["File 1"]
    },
    roomSharing: {
      shareable: true,
      info: ["Info 1"],
      files: ["File 1"]
    },
    warnings: []
  },
];

export { arrayOfSheets };