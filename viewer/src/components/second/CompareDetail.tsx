/** The comparison in detail — behind a disclosure, below the build.
 *
 * Reads the same SideBySideData as the verdict sentence and the old table,
 * but speaks only in what the god page is allowed to show: gold, percent of
 * players, and the comparison's own percentages. The model's 0-1 scores
 * (`model.text`: "quality 0.584 ... 0.024 short") are deliberately not
 * rendered here; they live on the Method page's terms, not the player's.
 *
 * The community's six is NOT listed again: the "Community" tab already
 * shows it in place. What this adds is per-scenario percentages, the items
 * that differ and what each one does, and what the model can't see. */
import type { SideBySideData } from "../SideBySide";
import type { CommunityBuildEntry } from "../../types";
import type { ComparisonMeta } from "./useComparison";
import { Art } from "./art";

type Metric = "burst_squishy" | "burst_tank" | "sustained_squishy" | "sustained_tank" | "ehp_physical" | "ehp_magical";

const ROWS: { key: Metric; label: string }[] = [
  { key: "burst_squishy", label: "Burst combo into a squishy" },
  { key: "burst_tank", label: "Burst combo into a tank" },
  { key: "sustained_squishy", label: "10 seconds of damage, squishy" },
  { key: "sustained_tank", label: "10 seconds of damage, tank" },
  { key: "ehp_physical", label: "Health against physical" },
  { key: "ehp_magical", label: "Health against magical" },
];

const signedPct = (r: number) => {
  const p = (r - 1) * 100;
  if (Math.abs(p) < 0.5) return "same";
  return `${p > 0 ? "+" : "−"}${Math.abs(p).toFixed(0)}%`;
};
const gold = (n: number) => Math.round(n).toLocaleString("en-US");

export function CompareDetail({ d, meta, god, community }: {
  d: SideBySideData; meta: ComparisonMeta | null; god: string; community?: CommunityBuildEntry;
}) {
  const band = meta?.band ?? 0.05;
  const tone = (r: number) => (r > 1 + band ? "text-positive" : r < 1 - band ? "text-negative" : "text-muted");
  const share = (name: string) => {
    const all = [...(community?.slot_order ?? []), ...(community?.popular_items ?? [])].filter((p) => p.name === name);
    return all.length ? Math.max(...all.map((p) => p.pick_rate)) : null;
  };
  const gaps = [...d.ichor.passives, ...d.community.passives]
    .filter((p) => p.status === "not simulated" || p.status === "partial");
  const uniqueGaps = gaps.filter((p, i) => gaps.findIndex((q) => q.item === p.item) === i);

  return (
    <div data-testid="compare-detail" className="space-y-6">
      <div>
        <h3 className="font-cond text-[22px] font-extrabold text-ink">Ichor&rsquo;s six against theirs</h3>
        <p className="mt-1 text-note text-muted">
          With all six bought, how much more or less Ichor&rsquo;s build does in each fight (the
          sentence up top also weighs the two- and four-item points). Within ±{Math.round(band * 100)}% counts as about even.
        </p>
        <table className="mt-3 w-full border-collapse text-copy">
          <caption className="sr-only">Ichor&rsquo;s six compared with the community&rsquo;s, per scenario</caption>
          <thead>
            <tr className="text-left text-cap text-quiet">
              <th scope="col" className="pb-2 font-medium">Fight</th>
              <th scope="col" className="pb-2 text-right font-medium">Ichor vs theirs</th>
            </tr>
          </thead>
          <tbody>
            {ROWS.map(({ key, label }) => {
              const r = d.community[key] ? d.ichor[key] / d.community[key] : 1;
              return (
                <tr key={key} className="border-t border-line">
                  <th scope="row" className="py-2.5 text-left font-normal text-ink">{label}</th>
                  <td className={`num py-2.5 text-right font-cond text-[20px] font-bold ${tone(r)}`}>{signedPct(r)}</td>
                </tr>
              );
            })}
            <tr className="border-t border-line">
              <th scope="row" className="py-2.5 text-left font-normal text-ink">Gold for the six</th>
              <td className="num py-2.5 text-right text-copy text-muted">
                {gold(d.ichor.gold)} <span className="text-quiet">vs</span> {gold(d.community.gold)}
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      {d.diffs.length > 0 && (
        <div>
          <h3 className="font-cond text-[22px] font-extrabold text-ink">Where the two sixes differ</h3>
          <ul className="mt-2 divide-y divide-line">
            {d.diffs.map((x) => {
              const s = x.community.pick_rate || share(x.item);
              return (
                <li key={`${x.side}-${x.item}`} className="grid grid-cols-[40px_minmax(0,1fr)] gap-3 py-3">
                  <Art name={x.item} kind="item" className="h-10 w-10 rounded-[8px]" />
                  <div className="min-w-0">
                    <p className="flex flex-wrap items-baseline gap-x-2">
                      <span className="font-cond text-[19px] font-bold text-ink">{x.item}</span>
                      <span className="text-cap text-quiet">{x.side === "ichor" ? "only in Ichor's" : "only in theirs"}</span>
                    </p>
                    <p className="text-note text-muted">
                      {s ? `${Math.round(s * 100)}% of ${god} players buy it` : `${god}'s players don't buy it`}
                      {x.passive.summary ? ` · ${x.passive.summary}` : ""}
                      {x.passive.status !== "simulated" ? ` · ${x.passive.status}` : ""}
                    </p>
                    {x.best_swap && (
                      <p className="mt-0.5 text-note text-muted">
                        In Ichor&rsquo;s six for {x.best_swap.replaces}: damage{" "}
                        <span className={tone(x.best_swap.damage_axis)}>{signedPct(x.best_swap.damage_axis)}</span>, survival{" "}
                        <span className={tone(x.best_swap.survival_axis)}>{signedPct(x.best_swap.survival_axis)}</span>
                      </p>
                    )}
                  </div>
                </li>
              );
            })}
          </ul>
        </div>
      )}

      {uniqueGaps.length > 0 && (
        <div data-testid="not-simulated">
          <h3 className="font-cond text-[22px] font-extrabold text-ink">Not measured here</h3>
          <p className="mt-1 text-note text-muted">
            The combat model can&rsquo;t play these passives yet, so their value is missing from the
            percentages above — not zero, unmeasured.
          </p>
          <ul className="mt-2 space-y-1.5 text-note">
            {uniqueGaps.map((p) => (
              <li key={p.item}><span className="font-semibold text-ink">{p.item}</span>{" "}
                <span className="text-muted">— {p.status}{p.assumptions.length ? `: ${p.assumptions.join("; ")}` : p.summary ? `: ${p.summary}` : ""}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {d.coverage && (
        <p className="text-note text-muted">
          The model simulates {Math.round(d.coverage.ichor * 100)}% of the gold in Ichor&rsquo;s six and{" "}
          {Math.round(d.coverage.community * 100)}% of the community&rsquo;s.
          {d.substitutions.some((s) => s.used) && (
            <> Their six was cleaned of components first: {d.substitutions.filter((s) => s.used)
              .map((s) => `${s.dropped} → ${s.used}`).join(", ")}.</>
          )}
        </p>
      )}
      {meta && (
        <p className="text-cap text-quiet">
          Level {meta.level}, one target for {meta.window} seconds, no crowd control. Squishy is a typical{" "}
          {meta.targets.squishy.role} ({gold(meta.targets.squishy.max_health)} health), tank a typical{" "}
          {meta.targets.tank.role} ({gold(meta.targets.tank.max_health)} health). Data: {meta.data}.
        </p>
      )}
    </div>
  );
}
