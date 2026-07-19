export function Footer() {
  return (
    <div className="border-t border-line px-4 py-2 text-[10px] text-muted">
      Build data derived from{" "}
      <a href="https://wiki.smite2.com" className="text-blue hover:underline" target="_blank" rel="noreferrer">wiki.smite2.com</a>
      {" "}and{" "}
      <a href="https://smitebrain.com" className="text-blue hover:underline" target="_blank" rel="noreferrer">SmiteBrain</a>.
      Suggested builds are heuristic — not official. A fan project, not affiliated with Hi-Rez.
    </div>
  );
}
