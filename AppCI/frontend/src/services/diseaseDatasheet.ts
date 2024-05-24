interface DiseaseDatasheet {
  name: string;
  type: string;
  cautions: String[];
  cleaning: String[];
  isolationTime: String;
  mandatoryNotification: Boolean;
  roomSharing: Boolean;
  warnings: String[];
};

let sheet : DiseaseDatasheet = {
  name: "COVID-19",
  type: "Virus",
  cautions: ["Wear a mask", "Wash your hands", "Avoid close contact"],
  cleaning: ["Clean and disinfect frequently touched surfaces"],
  isolationTime: "14 days",
  mandatoryNotification: true,
  roomSharing: false,
  warnings: ["COVID-19 is highly contagious", "COVID-19 can be deadly"]
};

let arrayOfSheets : DiseaseDatasheet[] = [
  sheet,
  {
    name: "Influenza",
    type: "Virus",
    cautions: ["Wear a mask", "Wash your hands", "Avoid close contact"],
    cleaning: ["Clean and disinfect frequently touched surfaces"],
    isolationTime: "5 days",
    mandatoryNotification: false,
    roomSharing: true,
    warnings: ["Influenza is highly contagious", "Influenza can be deadly"]
  },
];

export { DiseaseDatasheet, arrayOfSheets };