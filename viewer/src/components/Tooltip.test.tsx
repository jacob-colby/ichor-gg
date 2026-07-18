import { it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { Tooltip } from "./Tooltip";

it("shows tooltip content on focus and hides on blur", () => {
  render(
    <Tooltip content={<span>Cost 2900</span>}>
      <button>Deathbringer</button>
    </Tooltip>,
  );
  const trigger = screen.getByText("Deathbringer");
  fireEvent.focus(trigger);
  expect(screen.getByRole("tooltip")).toHaveTextContent("Cost 2900");
  fireEvent.blur(trigger);
  expect(screen.queryByRole("tooltip")).toBeNull();
});
