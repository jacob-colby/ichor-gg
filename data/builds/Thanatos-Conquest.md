---
type: smite-build
god: Thanatos
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reaping
  aspect_pick_rate: 0.38
  aspect_win_rate: 0.58
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.64
    win_rate: 0.47
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.1
      win_rate: 0.4
    - name: Daybreak Gavel
      pick_rate: 0.08
      win_rate: 0.5
  - name: The Reaper
    pick_rate: 0.3
    win_rate: 0.47
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.26
      win_rate: 0.46
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.83
  - name: Hydra's Lament
    pick_rate: 0.16
    win_rate: 0.63
    alternates:
    - name: The Reaper
      pick_rate: 0.18
      win_rate: 0.56
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.17
    win_rate: 0.63
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.13
      win_rate: 0.17
    - name: Titan's Bane
      pick_rate: 0.13
      win_rate: 0.67
  - name: Titan's Bane
    pick_rate: 0.16
    win_rate: 0.71
    alternates:
    - name: Heartseeker
      pick_rate: 0.11
      win_rate: 0.2
    - name: Lucerne Hammer
      pick_rate: 0.09
      win_rate: 0.25
  - name: Skeggox
    pick_rate: 0.07
    win_rate: 1.0
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.0
    - name: Magi's Cloak
      pick_rate: 0.07
      win_rate: 1.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.38
    win_rate: 0.63
  - name: Bumba's Cudgel
    pick_rate: 0.28
    win_rate: 0.36
  - name: Hunter's Cowl
    pick_rate: 0.1
    win_rate: 0.4
  source_url: https://smitebrain.com/gods/thanatos/
  last_verified: '2026-08-26'
  god_win_rate: 0.5
  god_matches_won: 25
  god_matches_played: 50
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
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
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Pendulum Blade, Avatar''s Parashu, Tekko-Kagi, Tyrfing,
    Arondight, Transcendence, Runeforged Hammer, Avenging Blade, Golden Blade, Lernaean
    Bow, Shield Splitter, Dominance, Silverbranch Bow, Oath-Sworn Spear, Riptalon,
    Barbed Carver, Toxic Blade, Bloodforge, Deathbringer, Eye of the Storm, Damaru,
    Rage, Musashi''s Dual Swords, Sanguine Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.47
      pick: 0.64
      fit: 1.0
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.59
      efficiency: 0.54
      win: 0.63
      pick: 0.25
      fit: 0.71
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.61
      efficiency: 0.47
      win: 0.63
      pick: 0.28
      fit: 1.0
    Titan's Bane:
      total: 0.65
      efficiency: 0.47
      win: 0.71
      pick: 0.35
      fit: 1.0
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Magi's Cloak
  - Transcendence
  - Hydra's Lament
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Magi's Cloak
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: The
    Crusher, Transcendence, Arondight, Pendulum Blade, Avatar''s Parashu, Runeforged
    Hammer, Tyrfing, Tekko-Kagi, Avenging Blade, Dominance, Breastplate of Valor,
    Lernaean Bow, Genji''s Guard, Shield Splitter, Golden Blade, Oath-Sworn Spear,
    Silverbranch Bow, Barbed Carver, Riptalon, Bloodforge, Yogi''s Necklace, Toxic
    Blade, Deathbringer, Eye of the Storm, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.47
      pick: 0.64
      fit: 0.71
    Magi's Cloak:
      total: 0.55
      efficiency: 0.26
      win: 1.0
      pick: 0.22
      fit: 0.0
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.39
    Hydra's Lament:
      total: 0.58
      efficiency: 0.54
      win: 0.63
      pick: 0.25
      fit: 0.63
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.63
      pick: 0.28
      fit: 0.77
    Titan's Bane:
      total: 0.59
      efficiency: 0.47
      win: 0.71
      pick: 0.35
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Magi's Cloak
  - Transcendence
  - Hydra's Lament
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Magi's Cloak
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Pendulum Blade, The Crusher, Arondight, Avatar''s Parashu, Tekko-Kagi, Transcendence,
    Tyrfing, Runeforged Hammer, Silverbranch Bow, Avenging Blade, Breastplate of Valor,
    Riptalon, Genji''s Guard, Lernaean Bow, Toxic Blade, Shield Splitter, Dominance,
    Golden Blade, Oath-Sworn Spear, Barbed Carver, Eye of Erebus, Screeching Gargoyle,
    Bloodforge, Chandra''s Grace, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.47
      pick: 0.64
      fit: 0.78
    Magi's Cloak:
      total: 0.55
      efficiency: 0.26
      win: 1.0
      pick: 0.22
      fit: 0.0
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.22
    Hydra's Lament:
      total: 0.57
      efficiency: 0.54
      win: 0.63
      pick: 0.25
      fit: 0.54
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.63
      pick: 0.28
      fit: 0.76
    Titan's Bane:
      total: 0.6
      efficiency: 0.47
      win: 0.71
      pick: 0.35
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Magi's Cloak
  - Shifter's Shield
  - Heartseeker
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Shield of the Phoenix, Runeforged Hammer, Shield Splitter,
    Kinetic Cuirass, Eye of the Storm, Freya''s Tears, Berserker''s Shield, Erosion,
    Eye of Providence, Genji''s Guard, Breastplate of Valor, Draconic Scale, Yogi''s
    Necklace, Phoenix Feather, Avenging Blade, Stone of Binding, Midgardian Mail,
    Chandra''s Grace, Hide of the Nemean Lion, The Crusher, Leviathan''s Hide, Daybreak
    Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.47
      pick: 0.64
      fit: 0.44
    Magi's Cloak:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.22
      fit: 0.34
    Shifter's Shield:
      total: 0.66
      efficiency: 0.55
      win: 0.83
      pick: 0.16
      fit: 0.56
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.63
      pick: 0.28
      fit: 0.6
    Titan's Bane:
      total: 0.58
      efficiency: 0.47
      win: 0.71
      pick: 0.35
      fit: 0.5
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Magi's Cloak — magical protection
    swap_item: Magi's Cloak
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Avatar''s Parashu, Pendulum Blade, Tekko-Kagi, Avenging
    Blade, Silverbranch Bow, Riptalon, Oath-Sworn Spear, Tyrfing, Transcendence, Arondight,
    Toxic Blade, Runeforged Hammer, Lernaean Bow, Golden Blade, Shield Splitter, Dominance,
    Barbed Carver, Screeching Gargoyle, Bloodforge, Breastplate of Valor, Genji''s
    Guard, Deathbringer, Eye of the Storm, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.47
      pick: 0.64
      fit: 1.0
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.33
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.63
      pick: 0.25
      fit: 0.48
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.61
      efficiency: 0.47
      win: 0.63
      pick: 0.28
      fit: 1.0
    Titan's Bane:
      total: 0.65
      efficiency: 0.47
      win: 0.71
      pick: 0.35
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Magi's Cloak
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Titan's Bane
  flex_slots:
  - Tyrfing
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Tyrfing, Silverbranch Bow, Tekko-Kagi, Lernaean Bow, Golden
    Blade, Toxic Blade, Dominance, Qin''s Blade, The Crusher, Sun Beam Bow, Transcendence,
    Berserker''s Shield, Avatar''s Parashu, Dagger of Frenzy, Arondight, Runeforged
    Hammer, Pendulum Blade, Avenging Blade, Barbed Carver, Vital Amplifier, Hastened
    Fatalis, Bloodforge, The Executioner, Odysseus'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.47
      pick: 0.64
      fit: 0.37
    Magi's Cloak:
      total: 0.55
      efficiency: 0.26
      win: 1.0
      pick: 0.22
      fit: 0.0
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.56
      pick: 0.0
      fit: 0.79
    Riptalon:
      total: 0.55
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.69
    Titan's Bane:
      total: 0.57
      efficiency: 0.47
      win: 0.71
      pick: 0.35
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Magi's Cloak
  - Hydra's Lament
  - Pendulum Blade
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Pendulum Blade
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
    of Valor, Genji''s Guard, The Crusher, Avatar''s Parashu, Eye of Erebus, Transcendence,
    Tyrfing, Screeching Gargoyle, Runeforged Hammer, Chandra''s Grace, Freya''s Tears,
    Tekko-Kagi, Avenging Blade, Shield of the Phoenix, Silverbranch Bow, Lernaean
    Bow, Riptalon, Gladiator''s Shield, Shield Splitter, Dominance, Golden Blade,
    Prophetic Cloak, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.47
      pick: 0.64
      fit: 0.85
    Magi's Cloak:
      total: 0.55
      efficiency: 0.26
      win: 1.0
      pick: 0.22
      fit: 0.0
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.63
      pick: 0.25
      fit: 0.75
    Pendulum Blade:
      total: 0.53
      efficiency: 0.42
      win: 0.56
      pick: 0.0
      fit: 0.85
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.63
      pick: 0.28
      fit: 0.55
    Titan's Bane:
      total: 0.57
      efficiency: 0.47
      win: 0.71
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
    Underrated for this god: The Crusher, Pendulum Blade, Avatar''s Parashu, Tekko-Kagi,
    Tyrfing, Arondight, Transcendence, Runeforged Hammer, Avenging Blade, Golden Blade,
    Lernaean Bow, Shield Splitter, Dominance, Silverbranch Bow, Oath-Sworn Spear,
    Riptalon, Barbed Carver, Toxic Blade, Bloodforge, Deathbringer, Eye of the Storm,
    Damaru, Rage, Musashi''s Dual Swords, Sanguine Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.47
      pick: 0.64
      fit: 1.0
    The Reaper:
      total: 0.54
      efficiency: 0.5
      win: 0.47
      pick: 0.41
      fit: 0.91
    Pendulum Blade:
      total: 0.55
      efficiency: 0.42
      win: 0.56
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.61
      efficiency: 0.47
      win: 0.63
      pick: 0.28
      fit: 1.0
    Titan's Bane:
      total: 0.65
      efficiency: 0.47
      win: 0.71
      pick: 0.35
      fit: 1.0
  starter: *id001
---
