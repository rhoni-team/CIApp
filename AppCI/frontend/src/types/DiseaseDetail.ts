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

export interface DiseaseDetail {
    id: number;
    name: string;
    type: string | null;
    info: any[]; // eslint-disable-line @typescript-eslint/no-explicit-any
    cautions: {
      precautions: Precautions;
      list: string;
      info: any[]; // eslint-disable-line @typescript-eslint/no-explicit-any
      files: any[]; // eslint-disable-line @typescript-eslint/no-explicit-any
    };
    cleaning: {
      cleaning_type: CleaningType[];
      list: string[];
      info: any[]; // eslint-disable-line @typescript-eslint/no-explicit-any
      files: any[]; // eslint-disable-line @typescript-eslint/no-explicit-any
    };
    isolation: {
      isolationTime: number;
      isolationPeriod: string;
      info: any[]; // eslint-disable-line @typescript-eslint/no-explicit-any
      files: any[]; // eslint-disable-line @typescript-eslint/no-explicit-any
    };
    mandatoryNotification: {
      notify: boolean;
      info: any[]; // eslint-disable-line @typescript-eslint/no-explicit-any
      files: any[]; // eslint-disable-line @typescript-eslint/no-explicit-any
    };
    other_isolation: string;
    roomSharing: {
      shareable: boolean;
      info: any[]; // eslint-disable-line @typescript-eslint/no-explicit-any
      files: any[]; // eslint-disable-line @typescript-eslint/no-explicit-any
    };
    warnings: string[];
    withAtb: boolean;
  }
