/** Layout-shaped loading placeholders.
 *
 * A centered "Loading…" is the clearest tell that something is a script with a
 * UI rather than a site. These mirror the real layout so the page doesn't jump
 * when data lands. Animation is a slow opacity pulse — no spinners, and it
 * respects prefers-reduced-motion via the shared `motion-safe` variant.
 */

function Bar({ className = "" }: { className?: string }) {
  return <div className={`rounded bg-bg2 motion-safe:animate-pulse ${className}`} />;
}

/** Sidebar: a 4-column grid of god-card placeholders. */
export function GodSidebarSkeleton({ count = 12 }: { count?: number }) {
  return (
    <div aria-hidden="true" className="p-3">
      <Bar className="mb-3 h-9 w-full" />
      <div className="grid grid-cols-4 gap-2">
        {Array.from({ length: count }, (_, i) => (
          <div key={i} className="flex flex-col items-center gap-1.5 rounded-xl border border-line bg-bg2/40 p-2">
            <Bar className="h-11 w-11 rounded-md" />
            <Bar className="h-2 w-10" />
          </div>
        ))}
      </div>
    </div>
  );
}

/** Build page: header block plus a column of slot rows. */
export function BuildSkeleton({ rows = 6 }: { rows?: number }) {
  return (
    <div aria-hidden="true" className="p-4">
      <div className="mb-5 flex items-center gap-3">
        <Bar className="h-13 w-13 rounded-lg" />
        <div className="flex flex-col gap-2">
          <Bar className="h-5 w-40" />
          <Bar className="h-3 w-28" />
        </div>
      </div>
      <Bar className="mb-3 h-3 w-24" />
      <div className="flex flex-col gap-2">
        {Array.from({ length: rows }, (_, i) => (
          <div key={i} className="flex items-center gap-3 rounded-md p-1.5">
            <Bar className="h-8 w-8 rounded-sm" />
            <Bar className="h-3 flex-1 max-w-56" />
          </div>
        ))}
      </div>
    </div>
  );
}

/** Item/tier grids. */
export function CardGridSkeleton({ count = 10 }: { count?: number }) {
  return (
    <div aria-hidden="true" className="grid grid-cols-[repeat(auto-fill,minmax(140px,1fr))] gap-2.5 p-4 sm:grid-cols-[repeat(auto-fill,minmax(180px,1fr))]">
      {Array.from({ length: count }, (_, i) => (
        <div key={i} className="flex flex-col gap-2 rounded-md border border-line bg-bg2/40 p-2.5">
          <div className="flex items-center gap-2">
            <Bar className="h-8 w-8 rounded-sm" />
            <Bar className="h-3 flex-1" />
          </div>
          <Bar className="h-2 w-16" />
        </div>
      ))}
    </div>
  );
}

/** Whole-app first paint: sidebar beside a build. */
export function AppSkeleton() {
  return (
    <div className="flex flex-1 overflow-hidden" data-testid="app-skeleton">
      <div className="hidden w-64 shrink-0 border-r border-line md:block">
        <GodSidebarSkeleton />
      </div>
      <div className="min-w-0 flex-1">
        <BuildSkeleton />
      </div>
    </div>
  );
}
