import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { CommunitySource } from "./CommunitySource";

/* "The community" is not one thing — an Obsidian+ win rate and a Deity one
 * describe different populations. These figures were being presented as
 * settled fact with none of that attached. */
describe("CommunitySource", () => {
  const source = {
    division: "obsidian",
    window_start: "2026-07-14",
    window_end: "2026-07-27",
    matches_analyzed: 17172,
  };

  it("names the division, the sample and the window", () => {
    render(<CommunitySource source={source} />);
    const line = screen.getByTestId("community-source");
    expect(line).toHaveTextContent(/17,172/);
    expect(line).toHaveTextContent(/Obsidian\+/);
    expect(line).toHaveTextContent(/14 Jul.*27 Jul/);
  });

  it("reads the date from the string's own parts, not through Date", () => {
    // `new Date("2026-07-14")` is midnight UTC, which renders as the 13th for
    // any reader west of UTC — silently misreporting the window.
    render(<CommunitySource source={{ ...source, window_start: "2026-01-01" }} />);
    expect(screen.getByTestId("community-source")).toHaveTextContent(/1 Jan/);
  });

  it("renders nothing at all when the index predates the scrape", () => {
    const { container } = render(<CommunitySource source={undefined} />);
    expect(container).toBeEmptyDOMElement();
  });

  it("still names the division when the window is missing", () => {
    render(<CommunitySource source={{ division: "deity" }} />);
    const line = screen.getByTestId("community-source");
    expect(line).toHaveTextContent(/Demigod\/Deity/);
    // No dangling separator where the dates would have been.
    expect(line.textContent).not.toMatch(/·\s*$/);
  });

  it("passes an unknown division through rather than inventing a label", () => {
    render(<CommunitySource source={{ division: "bronze" }} />);
    expect(screen.getByTestId("community-source")).toHaveTextContent(/bronze/);
  });
});
