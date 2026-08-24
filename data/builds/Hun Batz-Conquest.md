---
type: smite-build
god: Hun Batz
mode: Conquest
builds:
- source: community
  aspect: Aspect of Disruption
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.39
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.59
    win_rate: 0.46
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.22
      win_rate: 0.47
    - name: Transcendence
      pick_rate: 0.09
      win_rate: 0.39
  - name: Hydra's Lament
    pick_rate: 0.47
    win_rate: 0.46
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.18
      win_rate: 0.45
    - name: Transcendence
      pick_rate: 0.13
      win_rate: 0.49
  - name: The Reaper
    pick_rate: 0.12
    win_rate: 0.47
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.16
      win_rate: 0.39
    - name: The Crusher
      pick_rate: 0.12
      win_rate: 0.47
  - name: Heartseeker
    pick_rate: 0.35
    win_rate: 0.45
    alternates:
    - name: Titan's Bane
      pick_rate: 0.12
      win_rate: 0.47
    - name: Blinking Abyss
      pick_rate: 0.09
      win_rate: 0.39
  - name: Titan's Bane
    pick_rate: 0.16
    win_rate: 0.62
    alternates:
    - name: Heartseeker
      pick_rate: 0.21
      win_rate: 0.51
    - name: Blinking Abyss
      pick_rate: 0.09
      win_rate: 0.37
  - name: Blinking Abyss
    pick_rate: 0.12
    win_rate: 0.35
    alternates:
    - name: Avatar's Parashu
      pick_rate: 0.08
      win_rate: 0.44
    - name: Skeggox
      pick_rate: 0.07
      win_rate: 0.63
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.53
    win_rate: 0.49
  - name: Bumba's Cudgel
    pick_rate: 0.32
    win_rate: 0.4
  - name: Bumba's Golden Dagger
    pick_rate: 0.05
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/hun-batz/
  last_verified: '2026-08-24'
  god_win_rate: 0.4495192307692308
  god_matches_won: 187
  god_matches_played: 416
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-24'
  god_matches_analyzed: 17273
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Crusher
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Pendulum Blade, Tekko-Kagi, Tyrfing, Arondight, Runeforged Hammer, Avenging
    Blade, Golden Blade, Lernaean Bow, Shield Splitter, Dominance, Silverbranch Bow,
    Oath-Sworn Spear, Riptalon, Barbed Carver, Toxic Blade, Bloodforge, Deathbringer,
    Eye of the Storm, Damaru, Rage, Musashi''s Dual Swords, Sanguine Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.46
      pick: 0.59
      fit: 1.0
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.49
      pick: 0.18
      fit: 0.52
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.46
      pick: 0.64
      fit: 0.71
    The Crusher:
      total: 0.53
      efficiency: 0.47
      win: 0.47
      pick: 0.19
      fit: 1.0
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.45
      pick: 0.58
      fit: 1.0
    Titan's Bane:
      total: 0.61
      efficiency: 0.47
      win: 0.62
      pick: 0.35
      fit: 1.0
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Transcendence
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Arondight,
    Pendulum Blade, Tyrfing, Runeforged Hammer, Tekko-Kagi, Avenging Blade, Dominance,
    Breastplate of Valor, Lernaean Bow, Genji''s Guard, Shield Splitter, Golden Blade,
    Oath-Sworn Spear, Silverbranch Bow, Daybreak Gavel, Barbed Carver, Riptalon, Bloodforge,
    Yogi''s Necklace, Toxic Blade, Deathbringer, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.46
      pick: 0.59
      fit: 0.71
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.49
      pick: 0.18
      fit: 0.39
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.46
      pick: 0.64
      fit: 0.63
    The Crusher:
      total: 0.47
      efficiency: 0.47
      win: 0.47
      pick: 0.19
      fit: 0.57
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.45
      pick: 0.58
      fit: 0.77
    Titan's Bane:
      total: 0.55
      efficiency: 0.47
      win: 0.62
      pick: 0.35
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Crusher
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Pendulum Blade, Arondight, Tekko-Kagi, Tyrfing, Runeforged Hammer, Silverbranch
    Bow, Avenging Blade, Breastplate of Valor, Riptalon, Genji''s Guard, Lernaean
    Bow, Toxic Blade, Shield Splitter, Dominance, Golden Blade, Daybreak Gavel, Oath-Sworn
    Spear, Barbed Carver, Eye of Erebus, Screeching Gargoyle, Bloodforge, Chandra''s
    Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.46
      pick: 0.59
      fit: 0.78
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.49
      pick: 0.18
      fit: 0.22
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.46
      pick: 0.64
      fit: 0.54
    The Crusher:
      total: 0.48
      efficiency: 0.47
      win: 0.47
      pick: 0.19
      fit: 0.66
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.45
      pick: 0.58
      fit: 0.76
    Titan's Bane:
      total: 0.56
      efficiency: 0.47
      win: 0.62
      pick: 0.35
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Runeforged Hammer,
    Shield Splitter, Shifter''s Shield, Eye of the Storm, Freya''s Tears, Berserker''s
    Shield, Erosion, Eye of Providence, Genji''s Guard, Breastplate of Valor, Draconic
    Scale, Yogi''s Necklace, Phoenix Feather, Avenging Blade, Stone of Binding, Midgardian
    Mail, Chandra''s Grace, Daybreak Gavel, Hide of the Nemean Lion, Magi''s Cloak,
    Leviathan''s Hide.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.46
      pick: 0.59
      fit: 0.44
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.46
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.5
      efficiency: 0.53
      win: 0.46
      pick: 0.0
      fit: 0.73
    Runeforged Hammer:
      total: 0.49
      efficiency: 0.57
      win: 0.46
      pick: 0.0
      fit: 0.54
    Titan's Bane:
      total: 0.54
      efficiency: 0.47
      win: 0.62
      pick: 0.35
      fit: 0.5
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Crusher
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Pendulum Blade, Tekko-Kagi, Avenging Blade, Silverbranch Bow, Riptalon,
    Tyrfing, Oath-Sworn Spear, Toxic Blade, Arondight, Runeforged Hammer, Lernaean
    Bow, Golden Blade, Shield Splitter, Dominance, Barbed Carver, Screeching Gargoyle,
    Daybreak Gavel, Bloodforge, Breastplate of Valor, Genji''s Guard, Deathbringer,
    Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.46
      pick: 0.59
      fit: 1.0
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.49
      pick: 0.18
      fit: 0.33
    The Reaper:
      total: 0.54
      efficiency: 0.5
      win: 0.47
      pick: 0.19
      fit: 0.94
    The Crusher:
      total: 0.53
      efficiency: 0.47
      win: 0.47
      pick: 0.19
      fit: 1.0
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.45
      pick: 0.58
      fit: 1.0
    Titan's Bane:
      total: 0.61
      efficiency: 0.47
      win: 0.62
      pick: 0.35
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  - Titan's Bane
  flex_slots:
  - Silverbranch Bow
  - The Reaper
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
    Blade, Toxic Blade, Dominance, Qin''s Blade, Sun Beam Bow, Berserker''s Shield,
    Dagger of Frenzy, Arondight, Runeforged Hammer, Pendulum Blade, Avenging Blade,
    Barbed Carver, Vital Amplifier, Hastened Fatalis, Bloodforge, The Executioner,
    Odysseus'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.46
      pick: 0.59
      fit: 0.37
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.46
      pick: 0.0
      fit: 0.79
    The Reaper:
      total: 0.48
      efficiency: 0.55
      win: 0.47
      pick: 0.19
      fit: 0.44
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.46
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.53
      win: 0.46
      pick: 0.0
      fit: 0.69
    Titan's Bane:
      total: 0.53
      efficiency: 0.47
      win: 0.62
      pick: 0.35
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Pendulum Blade
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Arondight
  - Heartseeker
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
    + fit + win/pick). Underrated for this god: Pendulum Blade, Arondight, Breastplate
    of Valor, Genji''s Guard, Eye of Erebus, Tyrfing, Screeching Gargoyle, Runeforged
    Hammer, Chandra''s Grace, Freya''s Tears, Tekko-Kagi, Avenging Blade, Shield of
    the Phoenix, Silverbranch Bow, Daybreak Gavel, Lernaean Bow, Riptalon, Gladiator''s
    Shield, Shield Splitter, Dominance, Golden Blade, Prophetic Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.46
      pick: 0.59
      fit: 0.85
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.46
      pick: 0.64
      fit: 0.75
    Arondight:
      total: 0.48
      efficiency: 0.5
      win: 0.46
      pick: 0.0
      fit: 0.65
    Pendulum Blade:
      total: 0.48
      efficiency: 0.42
      win: 0.46
      pick: 0.0
      fit: 0.85
    Heartseeker:
      total: 0.48
      efficiency: 0.47
      win: 0.45
      pick: 0.58
      fit: 0.55
    Titan's Bane:
      total: 0.53
      efficiency: 0.47
      win: 0.62
      pick: 0.35
      fit: 0.45
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
    Underrated for this god: Pendulum Blade, Tekko-Kagi, Tyrfing, Arondight, Runeforged
    Hammer, Avenging Blade, Golden Blade, Lernaean Bow, Shield Splitter, Dominance,
    Silverbranch Bow, Oath-Sworn Spear, Riptalon, Barbed Carver, Toxic Blade, Bloodforge,
    Deathbringer, Eye of the Storm, Damaru, Rage, Musashi''s Dual Swords, Sanguine
    Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.46
      pick: 0.59
      fit: 1.0
    The Reaper:
      total: 0.53
      efficiency: 0.5
      win: 0.47
      pick: 0.19
      fit: 0.91
    Pendulum Blade:
      total: 0.51
      efficiency: 0.42
      win: 0.46
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.53
      efficiency: 0.47
      win: 0.47
      pick: 0.19
      fit: 1.0
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.45
      pick: 0.58
      fit: 1.0
    Titan's Bane:
      total: 0.61
      efficiency: 0.47
      win: 0.62
      pick: 0.35
      fit: 1.0
  starter: *id001
---
