---
type: smite-build
god: Nut
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cosmos
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.46
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.37
    win_rate: 0.49
    alternates:
    - name: Tyrfing
      pick_rate: 0.32
      win_rate: 0.52
    - name: Book of Thoth
      pick_rate: 0.06
      win_rate: 0.57
  - name: Bragi's Harp
    pick_rate: 0.18
    win_rate: 0.53
    alternates:
    - name: Staff of Myrddin
      pick_rate: 0.16
      win_rate: 0.5
    - name: Spear of Desolation
      pick_rate: 0.09
      win_rate: 0.6
  - name: Rod of Tahuti
    pick_rate: 0.13
    win_rate: 0.48
    alternates:
    - name: Soul Gem
      pick_rate: 0.1
      win_rate: 0.55
    - name: Barbed Carver
      pick_rate: 0.08
      win_rate: 0.46
  - name: Obsidian Shard
    pick_rate: 0.14
    win_rate: 0.45
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.22
      win_rate: 0.55
    - name: The Executioner
      pick_rate: 0.08
      win_rate: 0.58
  - name: Evil Eye
    pick_rate: 0.06
    win_rate: 0.41
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.15
      win_rate: 0.55
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.61
  - name: Hunter's Bow
    pick_rate: 0.05
    win_rate: 0.41
    alternates:
    - name: Evil Eye
      pick_rate: 0.06
      win_rate: 0.55
    - name: Void Shard
      pick_rate: 0.04
      win_rate: 0.45
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.24
    win_rate: 0.55
  - name: Archmage's Gem
    pick_rate: 0.22
    win_rate: 0.59
  - name: Conduit Gem
    pick_rate: 0.13
    win_rate: 0.43
  source_url: https://smitebrain.com/gods/nut/
  last_verified: '2026-08-11'
  god_win_rate: 0.5080875356803045
  god_matches_won: 534
  god_matches_played: 1051
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-11'
  god_matches_analyzed: 18835
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Bragi's Harp
  - Spear of Desolation
  - The Crusher
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Riptalon, Berserker''s
    Shield, Spear of the Magus, Lernaean Bow, Bracer of The Abyss, Genji''s Guard,
    The Cosmic Horror, Hydra''s Lament, Silverbranch Bow, Death Metal, Nimble Ring,
    Golden Blade, Blood-Bound Book, The Reaper, Breastplate of Valor, Tekko-Kagi,
    Bancroft''s Talon, Chronos'' Pendant, Dominance, Pharaoh''s Curse, Helm of Radiance,
    Runeforged Hammer, The World Stone, Doom Orb, Rod of Asclepius, Damaru, Dreamer''s
    Idol, Heartseeker, Jade Scepter, Kinetic Cuirass, Shogun''s Ofuda, Gem of Focus.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.49
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.45
    Bragi's Harp:
      total: 0.51
      efficiency: 0.44
      win: 0.53
      pick: 0.25
      fit: 0.71
    Spear of Desolation:
      total: 0.49
      efficiency: 0.52
      win: 0.49
      pick: 0.37
      fit: 0.48
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.45
    Soul Gem:
      total: 0.56
      efficiency: 0.59
      win: 0.55
      pick: 0.16
      fit: 0.68
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Bragi's Harp
  - Spear of Desolation
  - The Crusher
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Riptalon, Genji''s Guard,
    Spear of the Magus, Berserker''s Shield, Hydra''s Lament, The Cosmic Horror, Lernaean
    Bow, Silverbranch Bow, Breastplate of Valor, The Reaper, Bracer of The Abyss,
    Death Metal, Tekko-Kagi, Golden Blade, Chronos'' Pendant, Blood-Bound Book, Bancroft''s
    Talon, Nimble Ring, Heartseeker, Dominance, Pharaoh''s Curse, Runeforged Hammer,
    The World Stone, Doom Orb, Freya''s Tears, Dreamer''s Idol, Pendulum Blade, Damaru,
    Helm of Radiance, Gem of Focus, Kinetic Cuirass, Shield of the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.71
      win: 0.49
      pick: 0.0
      fit: 0.16
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.56
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.53
      pick: 0.25
      fit: 0.62
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.49
      pick: 0.37
      fit: 0.56
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.5
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.55
      pick: 0.16
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Berserker''s Shield, Riptalon, Shield
    of the Phoenix, Rod of Asclepius, Blood-Bound Book, Bancroft''s Talon, Jotunn''s
    Revenge, Genji''s Guard, Kinetic Cuirass, The Reaper, The Crusher, Pharaoh''s
    Curse, Chandra''s Grace, Breastplate of Valor, Oni Hunter''s Garb, Golden Blade,
    Spear of the Magus, Freya''s Tears, Lifebinder, Lernaean Bow, Shogun''s Ofuda,
    Hydra''s Lament, Runeforged Hammer, The Cosmic Horror, Bracer of The Abyss, Phoenix
    Feather, Spectral Armor, Helm of Radiance, Death Metal, Umbral Link, Silverbranch
    Bow, Jade Scepter, Shifter''s Shield, Erosion, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.71
      win: 0.49
      pick: 0.0
      fit: 0.17
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.49
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.59
      win: 0.49
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.64
    Soul Gem:
      total: 0.58
      efficiency: 0.59
      win: 0.55
      pick: 0.16
      fit: 0.79
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - The Crusher
  - Soul Gem
  flex_slots:
  - Spear of the Magus
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Riptalon, Spear
    of the Magus, The Cosmic Horror, Berserker''s Shield, Silverbranch Bow, The Reaper,
    Genji''s Guard, Tekko-Kagi, Lernaean Bow, Bracer of The Abyss, Hydra''s Lament,
    Avenging Blade, Death Metal, Screeching Gargoyle, The World Stone, Doom Orb, Breastplate
    of Valor, Dreamer''s Idol, Heartseeker, Golden Blade, Blood-Bound Book, Bancroft''s
    Talon, Nimble Ring, Chronos'' Pendant, Pharaoh''s Curse, Stone of Binding, Dominance,
    Toxic Blade, Runeforged Hammer, Titan''s Bane, Helm of Radiance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.49
      pick: 0.37
      fit: 0.57
    The Cosmic Horror:
      total: 0.5
      efficiency: 0.58
      win: 0.49
      pick: 0.0
      fit: 0.49
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.49
      pick: 0.0
      fit: 0.49
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.56
    Soul Gem:
      total: 0.57
      efficiency: 0.59
      win: 0.55
      pick: 0.16
      fit: 0.76
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Bragi's Harp
  - Riptalon
  - The Crusher
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Riptalon, Jotunn''s Revenge, The Crusher, Berserker''s
    Shield, Silverbranch Bow, Golden Blade, Genji''s Guard, Lernaean Bow, Spear of
    the Magus, Bracer of The Abyss, The Cosmic Horror, Hydra''s Lament, Death Metal,
    Breastplate of Valor, Nimble Ring, Blood-Bound Book, Bancroft''s Talon, Pharaoh''s
    Curse, The Reaper, Tekko-Kagi, Chronos'' Pendant, Dominance, Toxic Blade, Runeforged
    Hammer, Helm of Radiance, Kinetic Cuirass, Damaru, Rod of Asclepius, Amanita Charm,
    Shogun''s Ofuda, Oni Hunter''s Garb, Freya''s Tears, Jade Scepter, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.36
    Tyrfing:
      total: 0.5
      efficiency: 0.46
      win: 0.52
      pick: 0.32
      fit: 0.63
    Bragi's Harp:
      total: 0.5
      efficiency: 0.44
      win: 0.53
      pick: 0.25
      fit: 0.63
    Riptalon:
      total: 0.51
      efficiency: 0.56
      win: 0.49
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.5
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.38
    Soul Gem:
      total: 0.55
      efficiency: 0.59
      win: 0.55
      pick: 0.16
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Hydra's Lament
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Gluttonous Grimoire, Hydra''s Lament, Breastplate of Valor, The Crusher, Berserker''s
    Shield, Riptalon, Chronos'' Pendant, Freya''s Tears, Lernaean Bow, Spear of the
    Magus, Shield of the Phoenix, Silverbranch Bow, Bracer of The Abyss, The Cosmic
    Horror, Gem of Focus, Screeching Gargoyle, Golden Blade, Chandra''s Grace, Pendulum
    Blade, Pharaoh''s Curse, The Reaper, Death Metal, Blood-Bound Book, Arondight,
    Nimble Ring, Bancroft''s Talon, Tekko-Kagi, Dominance, Kinetic Cuirass, Runeforged
    Hammer, Amanita Charm, Oni Hunter''s Garb, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.49
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.6
    Hydra's Lament:
      total: 0.5
      efficiency: 0.58
      win: 0.49
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.51
      efficiency: 0.52
      win: 0.49
      pick: 0.37
      fit: 0.6
    Soul Gem:
      total: 0.58
      efficiency: 0.59
      win: 0.55
      pick: 0.16
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Spear of the Magus
  - The Crusher
  flex_slots:
  - Spear of the Magus
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher,
    Riptalon, Berserker''s Shield, Spear of the Magus, Lernaean Bow, Bracer of The
    Abyss, Genji''s Guard, The Cosmic Horror, Hydra''s Lament, Silverbranch Bow, Death
    Metal, Nimble Ring, Golden Blade, Blood-Bound Book, The Reaper, Breastplate of
    Valor, Tekko-Kagi, Bancroft''s Talon, Chronos'' Pendant, Dominance, Pharaoh''s
    Curse, Helm of Radiance, Runeforged Hammer, The World Stone, Doom Orb, Rod of
    Asclepius, Damaru, Dreamer''s Idol, Heartseeker, Jade Scepter, Kinetic Cuirass,
    Shogun''s Ofuda, Gem of Focus.'
  slot_scores:
    Lernaean Bow:
      total: 0.49
      efficiency: 0.54
      win: 0.49
      pick: 0.0
      fit: 0.52
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.49
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.58
    Spear of the Magus:
      total: 0.49
      efficiency: 0.6
      win: 0.49
      pick: 0.0
      fit: 0.38
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.49
      pick: 0.0
      fit: 0.45
  starter: *id001
---
