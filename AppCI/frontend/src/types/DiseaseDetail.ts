interface Precautions {
  id: number;
  name: string;
  label: string;
}

interface CleaningType {
  id: number;
  name: string;
  label: string;
}

interface Warnings {
  id: number;
  name: string;
  label: string;
}

export interface DiseaseDetail {
    id: number;
    name: string;
    type: string | null;
    info: string[];
    cautions: {
      precautions: Precautions;
      // list: string;
      info: string[]; 
      files: string[];
    };
    cleaning: {
      cleaning_type: CleaningType[];
      // list: string[];
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
    other_isolation: string;
    roomSharing: {
      shareable: boolean;
      info: string[];
      files: string[];
    };
    warnings: Warnings[];
    withAtb: boolean;
  }
