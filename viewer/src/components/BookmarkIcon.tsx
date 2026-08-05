/** The bookmark that marks one of your own gods.
 *
 * Was a pushpin, and lived privately inside `GodPicker`. It is now the mark
 * for a saved god everywhere one can appear — the picker, the shell's search,
 * the draft's god picker, the tier list and Home — so it is a shared component
 * rather than four drifting copies of a path.
 *
 * Drawn, not a glyph, and matched to the stroke vocabulary the rest of the app
 * already uses: 24 viewBox, `strokeWidth 2`, round caps and joins. `filled`
 * is the state: an outline means "you could save this", a solid means "saved".
 *
 * The stored data is still `smite:pinnedGods` and the hook is still `usePins`.
 * Only the icon and the words a reader sees changed; renaming the key would
 * have silently emptied everyone's list.
 */
export function BookmarkIcon({ filled, size = 13 }: { filled: boolean; size?: number }) {
  return (
    <svg
      viewBox="0 0 24 24" width={size} height={size}
      fill={filled ? "currentColor" : "none"}
      stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"
      aria-hidden="true"
    >
      <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" />
    </svg>
  );
}
