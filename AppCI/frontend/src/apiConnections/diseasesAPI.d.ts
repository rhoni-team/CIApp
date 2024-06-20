// diseasesAPI.d.ts
import type { DiseasesNames } from '../types/DiseasesNames';
import type { DiseaseDetail } from '../types/DiseaseDetail';

export function getDiseasesListAPI(): Promise<DiseasesNames[]>;
// eslint-disable-next-line no-unused-vars
export function getDetailedDiseaseAPI(diseaseId: string): Promise<DiseaseDetail>;
