---
type: smite-build
god: Xbalanque
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Tyrfing
    pick_rate: 1.0
    win_rate: 0.5
  - name: Bow
    pick_rate: 0.5
    win_rate: 1.0
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.5
      win_rate: 0.0
  - name: Hunter's Bow
    pick_rate: 0.5
    win_rate: 1.0
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.5
      win_rate: 0.0
  - name: Dominance
    pick_rate: 1.0
    win_rate: 0.0
  community_starters:
  - name: Death's Toll
    pick_rate: 1.0
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/xbalanque/
  last_verified: '2026-11-04'
  god_win_rate: 0.5
  god_matches_won: 1
  god_matches_played: 2
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-04'
  god_matches_analyzed: 149
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Tyrfing
  - Lernaean Bow
  - Musashi's Dual Swords
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Lernaean Bow, Demon Blade, Deathbringer, Musashi''s Dual
    Swords, Tekko-Kagi, Qin''s Blade, Rage, Sun Beam Bow, Riptalon, Hydra''s Lament,
    Bloodforge, Transcendence, The Reaper, Runeforged Hammer, Dagger of Frenzy, Toxic
    Blade, Jotunn''s Revenge, Barbed Carver, Avenging Blade, Shield Splitter, Vital
    Amplifier, Eye of the Storm, Arondight, Hastened Fatalis, The Crusher.'
  slot_scores:
    Golden Blade:
      total: 0.39
      efficiency: 0.47
      win: 0.25
      pick: 0.0
      fit: 0.73
    Tyrfing:
      total: 0.57
      efficiency: 0.5
      win: 0.5
      pick: 1.0
      fit: 0.83
    Lernaean Bow:
      total: 0.39
      efficiency: 0.51
      win: 0.25
      pick: 0.0
      fit: 0.64
    Musashi's Dual Swords:
      total: 0.36
      efficiency: 0.47
      win: 0.25
      pick: 0.0
      fit: 0.54
    Demon Blade:
      total: 0.37
      efficiency: 0.36
      win: 0.25
      pick: 0.0
      fit: 0.87
    Deathbringer:
      total: 0.36
      efficiency: 0.47
      win: 0.25
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Tyrfing
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Tekko-Kagi
  flex_slots:
  - The Reaper
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Tekko-Kagi, Hydra''s Lament, The Reaper, Titan''s Bane, Lernaean Bow,
    Heartseeker, The Crusher, Golden Blade, Arondight, Riptalon, Transcendence, Deathbringer,
    Musashi''s Dual Swords, Toxic Blade, Runeforged Hammer, Bloodforge, Rage, Demon
    Blade, Qin''s Blade, Pendulum Blade, Avatar''s Parashu, Avenging Blade, Shield
    Splitter, Eye of the Storm, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.41
      efficiency: 0.67
      win: 0.25
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.53
      efficiency: 0.5
      win: 0.5
      pick: 1.0
      fit: 0.53
    Transcendence:
      total: 0.33
      efficiency: 0.53
      win: 0.25
      pick: 0.0
      fit: 0.24
    Hydra's Lament:
      total: 0.37
      efficiency: 0.56
      win: 0.25
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.36
      efficiency: 0.56
      win: 0.25
      pick: 0.0
      fit: 0.35
    Tekko-Kagi:
      total: 0.37
      efficiency: 0.55
      win: 0.25
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Tyrfing
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Golden Blade
  - Tyrfing
  - Lernaean Bow
  - Musashi's Dual Swords
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Lernaean Bow, Golden Blade, Demon Blade, Deathbringer, Musashi''s Dual
    Swords, Rage, Tekko-Kagi, Qin''s Blade, Hydra''s Lament, Bloodforge, Sun Beam
    Bow, Riptalon, Transcendence, The Reaper, Runeforged Hammer, Jotunn''s Revenge,
    Dagger of Frenzy, Barbed Carver, Toxic Blade, Avenging Blade, Shield Splitter,
    Eye of the Storm, Arondight, Vital Amplifier, The Crusher, Hastened Fatalis.'
  slot_scores:
    Golden Blade:
      total: 0.38
      efficiency: 0.47
      win: 0.25
      pick: 0.0
      fit: 0.69
    Tyrfing:
      total: 0.57
      efficiency: 0.5
      win: 0.5
      pick: 1.0
      fit: 0.79
    Lernaean Bow:
      total: 0.38
      efficiency: 0.51
      win: 0.25
      pick: 0.0
      fit: 0.6
    Musashi's Dual Swords:
      total: 0.36
      efficiency: 0.47
      win: 0.25
      pick: 0.0
      fit: 0.57
    Demon Blade:
      total: 0.37
      efficiency: 0.36
      win: 0.25
      pick: 0.0
      fit: 0.88
    Deathbringer:
      total: 0.36
      efficiency: 0.47
      win: 0.25
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Tyrfing
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Tyrfing
  - Yogi's Necklace
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Yogi's Necklace
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Golden Blade, Kinetic Cuirass, Shield Splitter, Yogi''s
    Necklace, Phoenix Feather, Runeforged Hammer, Shield of the Phoenix, Pharaoh''s
    Curse, Bloodforge, Oni Hunter''s Garb, Shogun''s Ofuda, Lernaean Bow, The Reaper,
    Erosion, Eye of Providence, Midgardian Mail, Draconic Scale, Genji''s Guard, Riptalon,
    Leviathan''s Hide, Avenging Blade, Stone of Binding, Magi''s Cloak, Shifter''s
    Shield, Ancile, Umbral Link.'
  slot_scores:
    Golden Blade:
      total: 0.38
      efficiency: 0.52
      win: 0.25
      pick: 0.0
      fit: 0.59
    Tyrfing:
      total: 0.53
      efficiency: 0.5
      win: 0.5
      pick: 1.0
      fit: 0.54
    Yogi's Necklace:
      total: 0.37
      efficiency: 0.54
      win: 0.25
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.38
      efficiency: 0.56
      win: 0.25
      pick: 0.0
      fit: 0.5
    Shield Splitter:
      total: 0.37
      efficiency: 0.59
      win: 0.25
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.45
      efficiency: 0.65
      win: 0.25
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Tyrfing
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Toxic Blade
  - Tyrfing
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - Titan's Bane
  flex_slots:
  - Toxic Blade
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Tekko-Kagi, The Reaper, Riptalon, Titan''s Bane, Toxic Blade, Jotunn''s
    Revenge, The Crusher, Heartseeker, Lernaean Bow, Golden Blade, Avenging Blade,
    Avatar''s Parashu, Deathbringer, Musashi''s Dual Swords, Qin''s Blade, The Executioner,
    Demon Blade, Hydra''s Lament, Rage, Oath-Sworn Spear, Transcendence, Bloodforge,
    Runeforged Hammer, Sun Beam Bow, Pendulum Blade, Barbed Carver.'
  slot_scores:
    Toxic Blade:
      total: 0.37
      efficiency: 0.45
      win: 0.25
      pick: 0.0
      fit: 0.69
    Tyrfing:
      total: 0.54
      efficiency: 0.5
      win: 0.5
      pick: 1.0
      fit: 0.58
    Jotunn's Revenge:
      total: 0.37
      efficiency: 0.54
      win: 0.25
      pick: 0.0
      fit: 0.47
    The Reaper:
      total: 0.39
      efficiency: 0.56
      win: 0.25
      pick: 0.0
      fit: 0.56
    Tekko-Kagi:
      total: 0.41
      efficiency: 0.55
      win: 0.25
      pick: 0.0
      fit: 0.69
    Titan's Bane:
      total: 0.39
      efficiency: 0.54
      win: 0.25
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Tyrfing
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Tyrfing
  - Lernaean Bow
  - Qin's Blade
  - Tekko-Kagi
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Lernaean Bow, Qin''s Blade, Demon Blade, Tekko-Kagi, Deathbringer,
    Musashi''s Dual Swords, Sun Beam Bow, Hydra''s Lament, Rage, Riptalon, Bloodforge,
    Transcendence, Runeforged Hammer, Dagger of Frenzy, The Reaper, Toxic Blade, Jotunn''s
    Revenge, Avenging Blade, Barbed Carver, Vital Amplifier, Shield Splitter, Eye
    of the Storm, Hastened Fatalis, Arondight, The Executioner.'
  slot_scores:
    Golden Blade:
      total: 0.37
      efficiency: 0.47
      win: 0.25
      pick: 0.0
      fit: 0.65
    Tyrfing:
      total: 0.56
      efficiency: 0.5
      win: 0.5
      pick: 1.0
      fit: 0.75
    Lernaean Bow:
      total: 0.37
      efficiency: 0.51
      win: 0.25
      pick: 0.0
      fit: 0.55
    Qin's Blade:
      total: 0.35
      efficiency: 0.38
      win: 0.25
      pick: 0.0
      fit: 0.69
    Tekko-Kagi:
      total: 0.34
      efficiency: 0.46
      win: 0.25
      pick: 0.0
      fit: 0.45
    Demon Blade:
      total: 0.35
      efficiency: 0.36
      win: 0.25
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Tyrfing
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Golden Blade
  - Tyrfing
  - Lernaean Bow
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  flex_slots:
  - Lernaean Bow
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Hydra''s Lament,
    Arondight, Lernaean Bow, Golden Blade, Damaru, Genji''s Guard, Qin''s Blade, Deathbringer,
    Musashi''s Dual Swords, Tekko-Kagi, Breastplate of Valor, Demon Blade, Transcendence,
    Rage, Bloodforge, Chandra''s Grace, Runeforged Hammer, Sun Beam Bow, The Reaper,
    Riptalon, Avenging Blade, Shield Splitter, Dagger of Frenzy, Eye of Erebus, Barbed
    Carver.'
  slot_scores:
    Golden Blade:
      total: 0.34
      efficiency: 0.47
      win: 0.25
      pick: 0.0
      fit: 0.42
    Tyrfing:
      total: 0.53
      efficiency: 0.5
      win: 0.5
      pick: 1.0
      fit: 0.52
    Lernaean Bow:
      total: 0.35
      efficiency: 0.51
      win: 0.25
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.39
      efficiency: 0.63
      win: 0.25
      pick: 0.0
      fit: 0.41
    Hydra's Lament:
      total: 0.38
      efficiency: 0.56
      win: 0.25
      pick: 0.0
      fit: 0.51
    Arondight:
      total: 0.36
      efficiency: 0.54
      win: 0.25
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Tyrfing
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Rod of Tahuti, Death Metal, Soul Gem, Nimble
    Ring, Jotunn''s Revenge, Spear of Desolation, Obsidian Shard, Gluttonous Grimoire,
    Tekko-Kagi, Spear of the Magus, Blood-Bound Book, Bragi''s Harp, The Reaper, Ancient
    Signet, Hydra''s Lament, Titan''s Bane, Chronos'' Pendant, Bracer of The Abyss,
    Doom Orb, Lernaean Bow, The World Stone, Riptalon, Dreamer''s Idol, The Crusher,
    Golden Blade, Gem of Focus, Toxic Blade, Heartwood Charm, Arondight, Polynomicon,
    Bancroft''s Talon, Heartseeker, The Cosmic Horror, Deathbringer, Musashi''s Dual
    Swords, Soul Reaver, Typhon’s Heart, Qin''s Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.4
      efficiency: 0.67
      win: 0.25
      pick: 0.0
      fit: 0.36
    Tyrfing:
      total: 0.52
      efficiency: 0.5
      win: 0.5
      pick: 1.0
      fit: 0.49
    Death Metal:
      total: 0.41
      efficiency: 0.63
      win: 0.25
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.39
      efficiency: 0.59
      win: 0.25
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.47
      efficiency: 0.86
      win: 0.25
      pick: 0.0
      fit: 0.35
    Soul Gem:
      total: 0.41
      efficiency: 0.57
      win: 0.25
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Tyrfing
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Tyrfing
  - Death Metal
  - Nimble Ring
  - Tekko-Kagi
  - Obsidian Shard
  - Rod of Tahuti
  flex_slots:
  - Tekko-Kagi
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Death Metal, Nimble
    Ring, Tekko-Kagi, Gluttonous Grimoire, Obsidian Shard, Soul Gem, The Reaper, Bragi''s
    Harp, Titan''s Bane, Spear of the Magus, Lernaean Bow, Blood-Bound Book, Riptalon,
    Jotunn''s Revenge, Spear of Desolation, Golden Blade, Ancient Signet, The Crusher,
    Bracer of The Abyss, Doom Orb, The World Stone, Heartseeker, Toxic Blade, Dreamer''s
    Idol, Deathbringer, Musashi''s Dual Swords, Hydra''s Lament, Bancroft''s Talon,
    Polynomicon, Demon Blade, Transcendence, The Cosmic Horror, Rage, Bloodforge,
    Qin''s Blade, Runeforged Hammer, Avatar''s Parashu.'
  slot_scores:
    Tyrfing:
      total: 0.54
      efficiency: 0.5
      win: 0.5
      pick: 1.0
      fit: 0.6
    Death Metal:
      total: 0.42
      efficiency: 0.63
      win: 0.25
      pick: 0.0
      fit: 0.57
    Nimble Ring:
      total: 0.4
      efficiency: 0.63
      win: 0.25
      pick: 0.0
      fit: 0.46
    Tekko-Kagi:
      total: 0.39
      efficiency: 0.55
      win: 0.25
      pick: 0.0
      fit: 0.54
    Obsidian Shard:
      total: 0.38
      efficiency: 0.58
      win: 0.25
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.47
      efficiency: 0.86
      win: 0.25
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Tyrfing
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Tyrfing
  - Lernaean Bow
  - Dominance
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Demon Blade
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Golden Blade, Lernaean Bow, Demon Blade, Deathbringer,
    Musashi''s Dual Swords, Tekko-Kagi, Qin''s Blade, Rage, Sun Beam Bow, Riptalon,
    Hydra''s Lament, Bloodforge, Transcendence, The Reaper, Runeforged Hammer, Dagger
    of Frenzy, Toxic Blade, Jotunn''s Revenge, Barbed Carver, Avenging Blade, Shield
    Splitter, Vital Amplifier, Eye of the Storm, Arondight, Hastened Fatalis, The
    Crusher.'
  slot_scores:
    Golden Blade:
      total: 0.39
      efficiency: 0.47
      win: 0.25
      pick: 0.0
      fit: 0.73
    Tyrfing:
      total: 0.57
      efficiency: 0.5
      win: 0.5
      pick: 1.0
      fit: 0.83
    Lernaean Bow:
      total: 0.39
      efficiency: 0.51
      win: 0.25
      pick: 0.0
      fit: 0.64
    Dominance:
      total: 0.31
      efficiency: 0.47
      win: 0.0
      pick: 1.0
      fit: 0.64
    Demon Blade:
      total: 0.37
      efficiency: 0.36
      win: 0.25
      pick: 0.0
      fit: 0.87
    Deathbringer:
      total: 0.36
      efficiency: 0.47
      win: 0.25
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Tyrfing
  - Dominance
  starter: *id001
---
