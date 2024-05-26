import { describe, it, expect } from "vitest";
import { mount } from "@vue/test-utils";
import HomeView from "@/views/HomeView.vue";

describe("HomeView", () => {
  it("should render greeting to rhonies", () => {
    const wrapper = mount(HomeView);
    expect(wrapper.text()).toContain("Precauciones");
  })
});