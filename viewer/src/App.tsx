import { useEffect, useState } from "react";
import { useIndexData } from "./hooks/useIndexData";
import { Home } from "./components/Home";
import { DraftPage } from "./components/DraftPage";
import { DraftDock } from "./components/DraftDock";
import { DetailPanel } from "./components/DetailPanel";
import { AddGodModal } from "./components/AddGodModal";
import { ItemsShop } from "./components/ItemsShop";
import { GodInfo } from "./components/GodInfo";
import { GodItems } from "./components/GodItems";
import { GodRanking } from "./components/GodRanking";
import { GodPickerDialog } from "./components/GodPicker";
import { SubjectFrame, LensTabs } from "./components/SubjectFrame";
import { SubjectSearch } from "./components/SubjectSearch";
import { Legend } from "./components/Legend";
import { TierList } from "./components/TierList";
import { PatchNotes } from "./components/PatchNotes";
import { AppSkeleton, HomeSkeleton } from "./components/Skeleton";
import { relativeDate } from "./lib/relativeDate";
import { useHashRoute, toHash, navigate } from "./lib/useHashRoute";
import { documentTitle } from "./lib/documentTitle";
import { buildDivergenceBoard } from "./lib/divergence";
import type { CuratedBuildEntry } from "./types";

function App() {
  const { data, error, reload } = useIndexData();
  const route = useHashRoute();
  const [mode, setMode] = useState("Conquest");
  const [legendOpen, setLegendOpen] = useState(false);
  const [scraping, setScraping] = useState(false);
  const [addOpen, setAddOpen] = useState(false);
  const [pickerOpen, setPickerOpen] = useState(false);
  const isDev = import.meta.env.DEV;

  // Per-route tab/history title — these links get pasted into Discord, and a
  // history full of identical "ichor" entries is useless.
  useEffect(() => {
    document.title = documentTitle(route);
  }, [route]);

  // Changing subject closes the switcher; nothing else should.
  useEffect(() => { setPickerOpen(false); }, [route.god]);

  const godsApi = async (action: "add" | "remove", name: string) => {
    setScraping(true);
    const res = await fetch("/api/gods", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action, name }),
    }).then((r) => r.json()).catch(() => ({ ok: false }));
    setScraping(false);
    if (action === "remove" && name === route.god) navigate(toHash.home());
    reload();
    return res;
  };
  const removeGod = (name: string) => godsApi("remove", name);
  const addGod = async (name: string) => {
    setAddOpen(false);
    await godsApi("add", name);
  };

  if (error) {
    return (
      <div className="flex h-screen flex-col items-center justify-center gap-4 px-6 text-center text-ink">
        <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-gold font-display text-lead font-bold text-bg0">S2</div>
        <div className="max-w-[46ch]">
          <h1 className="font-display text-title font-bold text-ink">Couldn&rsquo;t load the build data</h1>
          <p className="mt-2 text-body leading-relaxed text-muted">
            ichor reads everything from a single data file, and that file didn&rsquo;t come back.
            It&rsquo;s usually a refresh away — if it keeps failing, the site is probably mid-deploy.
          </p>
        </div>
        <button type="button" onClick={reload} className="press rounded-md bg-gold px-4 py-1.5 text-body font-medium text-bg0">
          Try again
        </button>
        {/* The technical detail stays available without leading with it. */}
        <p className="font-mono text-label text-faint">{error}</p>
      </div>
    );
  }

  if (!data) {
    return (
      <div className="flex h-screen flex-col text-ink">
        {/* Same chrome as the loaded shell, so nothing jumps when index.json
            lands — only the content area is a placeholder. */}
        <header className="flex items-center gap-3 border-b border-line px-4 py-2.5 sm:px-6">
          <span className="font-display text-lead font-bold tracking-tight text-ink">ichor</span>
          <button type="button" onClick={reload} className="press ml-auto rounded-md bg-bg2 px-3 py-1.5 text-small text-muted hover:text-ink">Reload</button>
        </header>
        <div className="flex min-h-0 flex-1 overflow-hidden">
          {route.god
            ? <AppSkeleton />
            : <div className="flex-1 overflow-y-auto"><HomeSkeleton /></div>}
        </div>
      </div>
    );
  }

  const god = route.god ? data.gods.find((g) => g.name === route.god) : undefined;
  const missingGod = !!route.god && !god;

  // The frame states what's in the index; Home's claim states what the model
  // thinks of it. Both read the same board, so the two can't drift.
  const board = buildDivergenceBoard(data.tierlist?.gods);
  const roster = { total: data.gods.length, ranked: board.ranked, unranked: board.unranked };

  // Per-mode slice, never the Conquest-mirroring top level: Joust has no
  // community ratings at all, so reading `tierlist.gods` there would assert a
  // community score that doesn't exist for that mode.
  const modeSlice = (mode === "Joust" ? data.tierlist?.joust : data.tierlist?.conquest) ?? data.tierlist;
  const tierEntry = route.god ? modeSlice?.gods.find((g) => g.name === route.god) : undefined;

  // The god's own suggested core, so the items lens can be read against the
  // build rather than as a free-floating ranking.
  const godNotes = route.god ? data.builds.filter((b) => b.god === route.god) : [];
  const godNote = godNotes.find((n) => n.mode === mode) ?? godNotes[0];
  const godCore = (godNote?.builds.find(
    (b) => b.source === "suggested"
      && (b as CuratedBuildEntry).archetype === "core"
      && !(b as CuratedBuildEntry).fun,
  ) as CuratedBuildEntry | undefined)?.slot_order as string[] | undefined;

  const patchNotes = data.patch_notes ?? [];
  const pickGod = (name: string) => { setPickerOpen(false); navigate(toHash.god(name)); };

  return (
    <div className="flex h-screen flex-col text-ink">
      {/* First focusable on the page. */}
      <a href="#main"
        className="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-50 focus:rounded-md focus:bg-gold focus:px-3 focus:py-2 focus:font-display focus:text-body focus:font-semibold focus:text-bg0">
        Skip to content
      </a>

      <header className="flex flex-none items-center gap-3 border-b border-line px-4 py-2 sm:px-6 sm:py-2.5">
        <a href={toHash.home()} className="press shrink-0 py-1 font-display text-lead font-bold tracking-tight text-ink">
          ichor
        </a>
        {/* Only one of these two is ever in the accessibility tree — the
            other is display:none at its breakpoint. */}
        <LensTabs god={route.god && god ? route.god : undefined} lens={route.lens} compact
          testId="lens-tabs-bar" className="hidden min-w-0 shrink-0 lg:block" />
        <div className="ml-auto min-w-0 max-w-xs shrink lg:max-w-md">
          <SubjectSearch gods={data.gods} items={data.items} />
        </div>
        <div className="flex shrink-0 items-center gap-2">
          {data.data_updated && (
            <span data-testid="header-freshness" title={data.data_updated}
              className="hidden text-label text-faint lg:inline">
              Updated {relativeDate(data.data_updated)}{data.data_patch ? ` · ${data.data_patch}` : ""}
            </span>
          )}
          {isDev && (
            <button type="button" onClick={() => setAddOpen(true)}
              className="press hidden items-center justify-center gap-1.5 rounded-md border border-dashed border-line-strong px-2.5 py-1.5 text-small text-faint hover:text-muted md:flex">
              <span className="rounded-sm border border-line-strong px-1 py-px text-micro font-semibold uppercase tracking-wider">Dev</span>+ Add god
            </button>
          )}
          <button type="button" onClick={reload}
            className="press hidden rounded-md border border-line bg-bg2 px-3 py-1.5 text-small text-muted hover:text-ink sm:block">
            Reload
          </button>
          <button type="button" onClick={() => setLegendOpen(true)} aria-label="Help and credits"
            className="press rounded-md border border-line bg-bg2 px-2.5 py-1.5 text-small text-muted hover:text-ink">?</button>
        </div>
      </header>

      {/* Dev-only scraping banner — quiet tier, flat fade */}
      {isDev && scraping && (
        <div className="flex flex-none items-center justify-center gap-2 border-b border-dashed border-line-strong bg-bg1 px-3 py-1.5 text-label text-faint">
          <span className="rounded-sm border border-line-strong px-1.5 py-px text-micro font-semibold uppercase tracking-wider text-faint">Dev</span>
          Scraping new data… this can take a minute.
        </div>
      )}

      {/* `godName` is deliberately not passed: a name this index doesn't have
          is not a subject. Asserting one gave the frame a portrait, an h1 and
          four lens tabs leading nowhere, on top of content saying the god
          doesn't exist — two h1s making opposite claims. */}
      <SubjectFrame
        god={god}
        lens={route.lens}
        tierEntry={tierEntry}
        roster={roster}
        modeLabel={route.god ? (godNote?.mode ?? mode) : "Conquest"}
        onPickGod={() => setPickerOpen(true)}
      />

      <main id="main" tabIndex={-1} className="min-h-0 flex-1 overflow-y-auto focus:outline-none">
        {missingGod ? (
          <div className="mx-auto w-full max-w-[1440px] p-4 sm:p-6">
            <h1 className="font-display text-title font-bold text-ink">No god called “{route.god}”</h1>
            <p className="mt-2 max-w-[64ch] text-body leading-relaxed text-muted">
              Nothing in this index goes by that name. It may have been renamed or dropped since
              that link was made.
            </p>
            <button type="button" onClick={() => setPickerOpen(true)}
              className="press mt-3 rounded-md border border-line bg-bg2 px-3 py-1.5 text-small text-ink-soft hover:border-line-strong">
              Choose a god
            </button>
          </div>
        ) : god ? (
          <div className="mx-auto w-full max-w-[1440px] p-4 sm:p-6">
            {route.lens === "kit" ? (
              <GodInfo god={god} />
            ) : route.lens === "items" ? (
              <GodItems god={god.name} scores={data.god_item_scores?.[god.name]}
                items={data.items} core={godCore ?? []} />
            ) : route.lens === "ranking" ? (
              <GodRanking god={god.name} role={god.role} entries={modeSlice?.gods}
                modeLabel={godNote?.mode ?? mode} />
            ) : (
              <DetailPanel
                god={god.name}
                godData={god}
                items={data.items}
                builds={data.builds}
                mode={mode}
                onModeChange={setMode}
                starters={data.starters ?? []}
              />
            )}
          </div>
        ) : route.lens === "draft" ? (
          <DraftPage gods={data.gods} items={data.items} builds={data.builds}
            godItemScores={data.god_item_scores} draftConfig={data.draft} />
        ) : route.lens === "items" ? (
          <ItemsShop items={data.items} openItem={route.item}
            tierItems={data.tierlist?.items ?? []} goldValues={data.item_gold_values ?? {}} />
        ) : route.lens === "tiers" ? (
          <TierList tierlist={data.tierlist} />
        ) : route.lens === "patch" ? (
          <PatchNotes periods={patchNotes} />
        ) : (
          <Home data={data} />
        )}
      </main>

      {/* Suppressed only on the draft page itself — showing a shrunken copy
          of the board you're already looking at would be a second, redundant
          instance of the exact same controls. Everywhere else, the comp you
          built stays reachable and editable without navigating back to it. */}
      {route.lens !== "draft" && (
        <DraftDock gods={data.gods} items={data.items} builds={data.builds}
          godItemScores={data.god_item_scores} draftConfig={data.draft} />
      )}

      {legendOpen && <Legend onClose={() => setLegendOpen(false)} />}
      {pickerOpen && (
        <GodPickerDialog
          gods={data.gods}
          selectedGod={route.god ?? null}
          onPick={pickGod}
          onClose={() => setPickerOpen(false)}
          onRemove={isDev ? removeGod : undefined}
        />
      )}
      {isDev && addOpen && (
        <AddGodModal
          roster={data.roster ?? []}
          tracked={data.gods.map((g) => g.name)}
          onAdd={addGod}
          onClose={() => setAddOpen(false)}
        />
      )}
    </div>
  );
}

export default App;
