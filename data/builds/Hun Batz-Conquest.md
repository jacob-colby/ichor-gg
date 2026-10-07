---
type: smite-build
god: Hun Batz
mode: Conquest
builds:
- source: community
  aspect: Aspect of Disruption
  aspect_pick_rate: 0.04
  aspect_win_rate: 1.0
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.46
    win_rate: 0.75
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.31
      win_rate: 0.63
    - name: Transcendence
      pick_rate: 0.15
      win_rate: 0.75
  - name: Hydra's Lament
    pick_rate: 0.23
    win_rate: 0.67
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.27
      win_rate: 0.86
    - name: Transcendence
      pick_rate: 0.15
      win_rate: 0.75
  - name: Heartseeker
    pick_rate: 0.2
    win_rate: 0.4
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.24
      win_rate: 0.83
    - name: The Crusher
      pick_rate: 0.16
      win_rate: 0.75
  - name: Barbed Carver
    pick_rate: 0.21
    win_rate: 1.0
    alternates:
    - name: Heartseeker
      pick_rate: 0.21
      win_rate: 0.8
    - name: Blinking Abyss
      pick_rate: 0.17
      win_rate: 0.25
  - name: Infused Axe
    pick_rate: 0.17
    win_rate: 0.75
    alternates:
    - name: Heartseeker
      pick_rate: 0.21
      win_rate: 0.8
    - name: Titan's Bane
      pick_rate: 0.17
      win_rate: 0.5
  - name: Lucerne Hammer
    pick_rate: 0.2
    win_rate: 1.0
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.13
      win_rate: 0.5
    - name: Contagion
      pick_rate: 0.07
      win_rate: 1.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.58
    win_rate: 0.8
  - name: Bumba's Cudgel
    pick_rate: 0.19
    win_rate: 0.6
  - name: Bluestone Brooch
    pick_rate: 0.08
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/hun-batz/
  last_verified: '2026-10-07'
  god_win_rate: 0.7307692307692307
  god_matches_won: 19
  god_matches_played: 26
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-07'
  god_matches_analyzed: 939
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Barbed Carver
  - Pendulum Blade
  - The Crusher
  - Avatar's Parashu
  flex_slots:
  - Avatar's Parashu
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Pendulum Blade, Avatar''s Parashu, Tekko-Kagi, Tyrfing,
    Arondight, Runeforged Hammer, Avenging Blade, Golden Blade, Lernaean Bow, Shield
    Splitter, Dominance, Silverbranch Bow, Oath-Sworn Spear, Riptalon, Toxic Blade,
    Bloodforge, Deathbringer, Eye of the Storm, Damaru, Rage, Musashi''s Dual Swords,
    Sanguine Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.76
      efficiency: 0.72
      win: 0.75
      pick: 0.46
      fit: 1.0
    Transcendence:
      total: 0.61
      efficiency: 0.53
      win: 0.75
      pick: 0.2
      fit: 0.52
    Barbed Carver:
      total: 0.68
      efficiency: 0.34
      win: 1.0
      pick: 0.35
      fit: 0.62
    Pendulum Blade:
      total: 0.64
      efficiency: 0.42
      win: 0.75
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.66
      efficiency: 0.47
      win: 0.75
      pick: 0.25
      fit: 1.0
    Avatar's Parashu:
      total: 0.63
      efficiency: 0.45
      win: 0.75
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Barbed Carver
  - The Crusher
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Barbed Carver
  - Arondight
  - The Crusher
  flex_slots:
  - Transcendence
  - Arondight
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: The
    Reaper, Arondight, Pendulum Blade, Avatar''s Parashu, Tyrfing, Runeforged Hammer,
    Tekko-Kagi, Avenging Blade, Dominance, Breastplate of Valor, Lernaean Bow, Genji''s
    Guard, Shield Splitter, Golden Blade, Oath-Sworn Spear, Silverbranch Bow, Daybreak
    Gavel, Riptalon, Bloodforge, Yogi''s Necklace, Toxic Blade, Deathbringer, Eye
    of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.72
      efficiency: 0.72
      win: 0.75
      pick: 0.46
      fit: 0.71
    Transcendence:
      total: 0.59
      efficiency: 0.53
      win: 0.75
      pick: 0.2
      fit: 0.39
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.67
      pick: 0.31
      fit: 0.63
    Barbed Carver:
      total: 0.65
      efficiency: 0.34
      win: 1.0
      pick: 0.35
      fit: 0.39
    Arondight:
      total: 0.58
      efficiency: 0.5
      win: 0.75
      pick: 0.0
      fit: 0.43
    The Crusher:
      total: 0.6
      efficiency: 0.47
      win: 0.75
      pick: 0.25
      fit: 0.57
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Barbed Carver
  - The Crusher
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Barbed Carver
  - Pendulum Blade
  - The Crusher
  flex_slots:
  - Hydra's Lament
  - Transcendence
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Pendulum Blade, The Reaper, Arondight, Avatar''s Parashu, Tekko-Kagi, Tyrfing,
    Runeforged Hammer, Silverbranch Bow, Avenging Blade, Breastplate of Valor, Riptalon,
    Genji''s Guard, Lernaean Bow, Toxic Blade, Shield Splitter, Dominance, Golden
    Blade, Daybreak Gavel, Oath-Sworn Spear, Eye of Erebus, Screeching Gargoyle, Bloodforge,
    Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.73
      efficiency: 0.72
      win: 0.75
      pick: 0.46
      fit: 0.78
    Transcendence:
      total: 0.57
      efficiency: 0.53
      win: 0.75
      pick: 0.2
      fit: 0.22
    Hydra's Lament:
      total: 0.59
      efficiency: 0.54
      win: 0.67
      pick: 0.31
      fit: 0.54
    Barbed Carver:
      total: 0.64
      efficiency: 0.34
      win: 1.0
      pick: 0.35
      fit: 0.32
    Pendulum Blade:
      total: 0.6
      efficiency: 0.42
      win: 0.75
      pick: 0.0
      fit: 0.78
    The Crusher:
      total: 0.61
      efficiency: 0.47
      win: 0.75
      pick: 0.25
      fit: 0.66
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Barbed Carver
  - The Crusher
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Contagion
  - Kinetic Cuirass
  - Barbed Carver
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Runeforged Hammer,
    The Reaper, Shield Splitter, Shifter''s Shield, Eye of the Storm, Freya''s Tears,
    Berserker''s Shield, Erosion, Eye of Providence, Genji''s Guard, Breastplate of
    Valor, Draconic Scale, Yogi''s Necklace, Phoenix Feather, Avenging Blade, Stone
    of Binding, Midgardian Mail, Chandra''s Grace, Daybreak Gavel, Hide of the Nemean
    Lion, Magi''s Cloak, Leviathan''s Hide.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.72
      win: 0.75
      pick: 0.46
      fit: 0.44
    Contagion:
      total: 0.65
      efficiency: 0.39
      win: 1.0
      pick: 0.22
      fit: 0.32
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.56
      win: 0.75
      pick: 0.0
      fit: 0.66
    Barbed Carver:
      total: 0.64
      efficiency: 0.34
      win: 1.0
      pick: 0.35
      fit: 0.33
    Runeforged Hammer:
      total: 0.62
      efficiency: 0.57
      win: 0.75
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.7
      efficiency: 0.65
      win: 0.75
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Jotunn's Revenge
  - Contagion
  - Barbed Carver
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - Pendulum Blade
  - The Crusher
  - Avatar's Parashu
  flex_slots:
  - Pendulum Blade
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Avatar''s Parashu, Pendulum Blade, Tekko-Kagi, Avenging
    Blade, Silverbranch Bow, Riptalon, Tyrfing, Oath-Sworn Spear, Toxic Blade, Arondight,
    Runeforged Hammer, Lernaean Bow, Golden Blade, Shield Splitter, Dominance, Screeching
    Gargoyle, Daybreak Gavel, Bloodforge, Breastplate of Valor, Genji''s Guard, Deathbringer,
    Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.76
      efficiency: 0.72
      win: 0.75
      pick: 0.46
      fit: 1.0
    The Reaper:
      total: 0.65
      efficiency: 0.5
      win: 0.75
      pick: 0.0
      fit: 0.94
    Tekko-Kagi:
      total: 0.62
      efficiency: 0.41
      win: 0.75
      pick: 0.0
      fit: 0.94
    Pendulum Blade:
      total: 0.64
      efficiency: 0.42
      win: 0.75
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.66
      efficiency: 0.47
      win: 0.75
      pick: 0.25
      fit: 1.0
    Avatar's Parashu:
      total: 0.64
      efficiency: 0.45
      win: 0.75
      pick: 0.0
      fit: 0.94
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Barbed Carver
  - Riptalon
  - Silverbranch Bow
  - Tekko-Kagi
  flex_slots:
  - Silverbranch Bow
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
    this god: Riptalon, Tyrfing, Silverbranch Bow, Tekko-Kagi, Lernaean Bow, Golden
    Blade, The Reaper, Toxic Blade, Dominance, Qin''s Blade, Sun Beam Bow, Berserker''s
    Shield, Avatar''s Parashu, Dagger of Frenzy, Arondight, Runeforged Hammer, Pendulum
    Blade, Avenging Blade, Vital Amplifier, Hastened Fatalis, Bloodforge, The Executioner,
    Odysseus'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.75
      pick: 0.46
      fit: 0.37
    Tyrfing:
      total: 0.63
      efficiency: 0.48
      win: 0.75
      pick: 0.0
      fit: 0.79
    Barbed Carver:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.35
      fit: 0.37
    Riptalon:
      total: 0.63
      efficiency: 0.51
      win: 0.75
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.53
      win: 0.75
      pick: 0.0
      fit: 0.69
    Tekko-Kagi:
      total: 0.61
      efficiency: 0.49
      win: 0.75
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Jotunn's Revenge
  - Barbed Carver
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Barbed Carver
  - Arondight
  - Pendulum Blade
  - The Crusher
  flex_slots:
  - Arondight
  - The Crusher
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Pendulum Blade, Arondight, Breastplate
    of Valor, Genji''s Guard, The Reaper, Avatar''s Parashu, Eye of Erebus, Tyrfing,
    Screeching Gargoyle, Runeforged Hammer, Chandra''s Grace, Freya''s Tears, Tekko-Kagi,
    Avenging Blade, Shield of the Phoenix, Silverbranch Bow, Daybreak Gavel, Lernaean
    Bow, Riptalon, Gladiator''s Shield, Shield Splitter, Dominance, Golden Blade,
    Prophetic Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.74
      efficiency: 0.72
      win: 0.75
      pick: 0.46
      fit: 0.85
    Hydra's Lament:
      total: 0.62
      efficiency: 0.54
      win: 0.67
      pick: 0.31
      fit: 0.75
    Barbed Carver:
      total: 0.62
      efficiency: 0.34
      win: 1.0
      pick: 0.35
      fit: 0.25
    Arondight:
      total: 0.61
      efficiency: 0.5
      win: 0.75
      pick: 0.0
      fit: 0.65
    Pendulum Blade:
      total: 0.61
      efficiency: 0.42
      win: 0.75
      pick: 0.0
      fit: 0.85
    The Crusher:
      total: 0.58
      efficiency: 0.47
      win: 0.75
      pick: 0.25
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Barbed Carver
  - The Crusher
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Pendulum Blade
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Reaper, Pendulum Blade, Avatar''s Parashu, Tekko-Kagi,
    Tyrfing, Arondight, Runeforged Hammer, Avenging Blade, Golden Blade, Lernaean
    Bow, Shield Splitter, Dominance, Silverbranch Bow, Oath-Sworn Spear, Riptalon,
    Toxic Blade, Bloodforge, Deathbringer, Eye of the Storm, Damaru, Rage, Musashi''s
    Dual Swords, Sanguine Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.76
      efficiency: 0.72
      win: 0.75
      pick: 0.46
      fit: 1.0
    The Reaper:
      total: 0.65
      efficiency: 0.5
      win: 0.75
      pick: 0.0
      fit: 0.91
    Pendulum Blade:
      total: 0.64
      efficiency: 0.42
      win: 0.75
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.66
      efficiency: 0.47
      win: 0.75
      pick: 0.25
      fit: 1.0
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.4
      pick: 0.31
      fit: 1.0
    Titan's Bane:
      total: 0.56
      efficiency: 0.47
      win: 0.5
      pick: 0.37
      fit: 1.0
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
---
