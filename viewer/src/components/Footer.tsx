export function Footer() {
  return (
    <footer className="border-t border-line px-4 py-2 text-[10px] text-faint">
      Build data derived from{" "}
      <a href="https://wiki.smite2.com" className="inline-block rounded-sm py-1.5 underline decoration-line-strong underline-offset-2 hover:text-muted" target="_blank" rel="noreferrer">wiki.smite2.com</a>
      {" "}and{" "}
      <a href="https://smitebrain.com" className="inline-block rounded-sm py-1.5 underline decoration-line-strong underline-offset-2 hover:text-muted" target="_blank" rel="noreferrer">SmiteBrain</a>.
      Suggested builds are heuristic — not official. A fan project, not affiliated with Hi-Rez.
    </footer>
  );
}
