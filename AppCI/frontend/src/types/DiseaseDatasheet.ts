export default interface DiseaseDatasheet {
  name: string;
  type: string;
  cautions: {
    list: String[];
    info: String[];
    files: String[];
  };
  cleaning: {
    list: String[];
    info: String[];
    files: String[];
  };
  isolation: {
    isolationTime: Number;
    isolationPeriod: String;
    info: String[];
    files: String[];
  };
  mandatoryNotification: {
    notify: Boolean;
    info: String[];
    files: String[];
  };
  roomSharing: {
    shareable: Boolean;
    info: String[];
    files: String[];
  };
  warnings: String[];
};
