import { describe, it, expect } from "vitest";
import { mount } from "@vue/test-utils";
import HomeView from "@/views/HomeView.vue";
import DiseaseSearchInput from "@/components/DiseaseSearchInput.vue";
import DiseaseDatasheetComponent from "../DiseaseDatasheetComponent.vue";

describe("HomeView render correctly", () => {
  it("DiseaseSearchInput component loaded", () => {
    const wrapper = mount(HomeView);
    const diseaseSearchInputComponent = wrapper.findComponent(DiseaseSearchInput); // Find the component
    expect(diseaseSearchInputComponent.exists()).toBe(true);
  })
  it("DiseaseDatasheetComponent loaded", () => {
    const wrapper = mount(HomeView);
    const diseaseDatasheetComponent = wrapper.findComponent(DiseaseDatasheetComponent); // Find the component
    expect(diseaseDatasheetComponent.exists()).toBe(true);
  })
});