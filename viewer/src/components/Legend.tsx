export function Legend({ onClose }: { onClose: () => void }) {
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4" onClick={onClose}>
      <div
        className="max-h-[85vh] max-w-lg overflow-y-auto rounded-lg border border-line bg-bg1 p-5"
        onClick={(e) => e.stopPropagation()}
      >
        <h2 className="mb-3 font-display text-xl font-bold text-ink">How this works</h2>
        <ul className="flex flex-col gap-2 text-sm text-muted">
          <li><b className="text-ink">Pick a god</b> from the left rail to see builds; switch <b className="text-ink">Builds / Items</b> in the top nav.</li>
          <li><b className="text-ink">Suggested</b> tabs are our scoring engine's picks (a heuristic). <b className="text-ink">Community</b> is SmiteBrain's high-elo meta. <b className="text-ink">Your</b> saved builds are the named tabs.</li>
          <li><b className="text-ink">Flavors</b> (crit / burst / bruiser / anti-tank) re-weight the build; the <b className="text-ink">Aspect</b> toggle swaps to that god's aspect build; the <b className="text-ink">Conquest / Joust</b> toggle changes mode.</li>
          <li><b className="text-ink">BUILD ORDER</b> is a recommended buy order; <b className="text-ink">flex</b> slots are the ones situational swaps replace.</li>
          <li>The <b className="text-ink">Items</b> shop rates every item <b className="text-under">Underrated</b> / <b>Fair</b> / <b className="text-premium">Overrated</b> by gold efficiency, with filters.</li>
          <li>Your builds save in <b className="text-ink">your browser</b> (nothing is uploaded). Scores are heuristics — a fan project, not official.</li>
        </ul>
        <button type="button" onClick={onClose} className="mt-4 rounded bg-gold px-4 py-1.5 text-sm font-medium text-bg0">Got it</button>
      </div>
    </div>
  );
}
