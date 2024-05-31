export default interface DiseaseDatasheet {
  name: string;
  type: string;
  cautions: {
    list: string[];
    info: string[];
    files: string[];
  };
  cleaning: {
    list: string[];
    info: string[];
    files: string[];
  };
  isolation: {
    isolationTime: number;
    isolationPeriod: string;
    info: string[];
    files: string[];
  };
  mandatoryNotification: {
    notify: boolean;
    info: string[];
    files: string[];
  };
  roomSharing: {
    shareable: boolean;
    info: string[];
    files: string[];
  };
  warnings: string[];
  info: string[];
};
