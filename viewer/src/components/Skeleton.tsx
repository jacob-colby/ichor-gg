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

/** Home: the claim block over the lane board. Shaped like the real page — a
 * headline, a paragraph, a search field, then five ranked columns — so nothing
 * moves when the index lands. */
export function HomeSkeleton({ lanes = 5, rows = 6 }: { lanes?: number; rows?: number }) {
  return (
    <div aria-hidden="true" data-testid="home-skeleton" className="mx-auto w-full max-w-[1440px] px-4 pb-12 pt-7 sm:px-6 sm:pt-9">
      <div className="flex flex-col gap-6 border-b border-line pb-6 lg:flex-row lg:items-end lg:justify-between">
        <div className="min-w-0 flex-1">
          <Bar className="h-8 w-full max-w-[15ch] sm:h-10" />
          <Bar className="mt-3 h-8 w-full max-w-[18ch] sm:h-10" />
          <Bar className="mt-4 h-3 w-full max-w-[52ch]" />
          <Bar className="mt-2 h-3 w-full max-w-[48ch]" />
          <Bar className="mt-2 h-3 w-full max-w-[38ch]" />
        </div>
        <div className="flex shrink-0 flex-col gap-3 lg:items-end">
          <Bar className="h-9 w-full rounded-md sm:w-80" />
          <Bar className="h-2.5 w-52" />
        </div>
      </div>

      <div className="pt-7">
        <Bar className="h-4 w-40" />
        <Bar className="mt-2.5 h-2.5 w-72" />
        <div className="mt-4 grid grid-cols-1 gap-x-4 gap-y-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5">
          {Array.from({ length: lanes }, (_, l) => (
            <div key={l} className="min-w-0">
              <Bar className="h-3 w-16" />
              <Bar className="mt-1.5 h-2 w-28" />
              <div className="mt-3 flex flex-col gap-3 border-t border-line pt-2.5">
                {Array.from({ length: rows }, (_, r) => (
                  <div key={r} className="flex flex-col gap-1.5">
                    <div className="flex items-center gap-2">
                      <Bar className="h-5 w-5 rounded-md" />
                      <Bar className="h-2.5 flex-1" />
                      <Bar className="h-2 w-6" />
                    </div>
                    <Bar className="h-[3px] w-full rounded-none" />
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
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
