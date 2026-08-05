---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.53
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.49
    win_rate: 0.61
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.26
      win_rate: 0.63
    - name: Stampede
      pick_rate: 0.03
      win_rate: 0.71
  - name: Breastplate of Valor
    pick_rate: 0.19
    win_rate: 0.58
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.64
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.27
    win_rate: 0.53
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 0.74
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.59
  - name: Dwarven Plate
    pick_rate: 0.15
    win_rate: 0.69
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.61
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.8
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.56
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.12
      win_rate: 0.58
    - name: Glorious Pridwen
      pick_rate: 0.06
      win_rate: 0.54
  - name: Medal of Defense
    pick_rate: 0.05
    win_rate: 0.71
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.75
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 1.0
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-08-01'
  god_win_rate: 0.5912408759124088
  god_matches_won: 162
  god_matches_played: 274
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Stampede, Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s
    Shield, Gluttonous Grimoire, Jotunn''s Revenge, Oni Hunter''s Garb, Freya''s Tears,
    The Crusher, Shield Splitter, Hydra''s Lament, Shield of the Phoenix, Eye of the
    Storm, Erosion, Draconic Scale, Spectral Armor, Pharaoh''s Curse, Soul Gem, Avenging
    Blade, Golden Blade, Yogi''s Necklace, Leviathan''s Hide, Death Metal, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Hide of the Nemean Lion, Lernaean Bow,
    Helm of Radiance, Damaru, Rod of Asclepius, Shogun''s Ofuda, Magi''s Cloak, Ancile,
    Wyrmskin Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.27
      fit: 0.31
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.19
      fit: 0.31
    Runeforged Hammer:
      total: 0.58
      efficiency: 0.6
      win: 0.63
      pick: 0.26
      fit: 0.48
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.61
      pick: 0.49
      fit: 0.57
    Amanita Charm:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.57
    Stampede:
      total: 0.56
      efficiency: 0.52
      win: 0.71
      pick: 0.03
      fit: 0.37
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Shield of the Phoenix
  - Runeforged Hammer
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Genji's Guard
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s
    Shield, Eye of Providence, Soul Gem, Gluttonous Grimoire, Rod of Asclepius, Jotunn''s
    Revenge, Oni Hunter''s Garb, The Crusher, Chandra''s Grace, Hydra''s Lament, Eye
    of the Storm, Freya''s Tears, The Reaper, Shield Splitter, Erosion, Phoenix Feather,
    Spectral Armor, Avenging Blade, Draconic Scale, Golden Blade, Pharaoh''s Curse,
    Yogi''s Necklace, Lifebinder, Blood-Bound Book, Bancroft''s Talon, Leviathan''s
    Hide, Death Metal, Midgardian Mail, Riptalon, Hide of the Nemean Lion, Lernaean
    Bow, Shogun''s Ofuda, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.27
      fit: 0.28
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.8
    Runeforged Hammer:
      total: 0.59
      efficiency: 0.6
      win: 0.63
      pick: 0.26
      fit: 0.54
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.61
      pick: 0.49
      fit: 0.56
    Amanita Charm:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.86
    Stampede:
      total: 0.56
      efficiency: 0.52
      win: 0.71
      pick: 0.03
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Runeforged Hammer
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  - Stampede
  flex_slots:
  - Genji's Guard
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Amanita Charm,
    Kinetic Cuirass, Berserker''s Shield, Soul Gem, Avenging Blade, Eye of Providence,
    Stone of Binding, Oni Hunter''s Garb, Screeching Gargoyle, Hydra''s Lament, Void
    Shield, Freya''s Tears, Spear of the Magus, Shield Splitter, The Reaper, Void
    Stone, The Cosmic Horror, Shield of the Phoenix, Spectral Armor, Eye of the Storm,
    Spear of Desolation, Erosion, Heartseeker, Yogi''s Necklace, Pharaoh''s Curse,
    Draconic Scale, Riptalon, Obsidian Shard, Death Metal, Golden Blade, Leviathan''s
    Hide, Silverbranch Bow, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.27
      fit: 0.23
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.6
      win: 0.63
      pick: 0.26
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.61
      pick: 0.49
      fit: 0.42
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.56
    Stampede:
      total: 0.54
      efficiency: 0.52
      win: 0.71
      pick: 0.03
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Runeforged Hammer
  - Shifter's Shield
  - Stampede
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Golden Blade, Eye of Providence, Pharaoh''s Curse, Oni Hunter''s Garb, The Crusher,
    Jotunn''s Revenge, Riptalon, Freya''s Tears, Lernaean Bow, Hydra''s Lament, Soul
    Gem, Shogun''s Ofuda, Shield of the Phoenix, Tyrfing, Silverbranch Bow, Spectral
    Armor, Shield Splitter, Yogi''s Necklace, Erosion, Eye of the Storm, Draconic
    Scale, Bracer of The Abyss, Dominance, Death Metal, Leviathan''s Hide, Rod of
    Asclepius, Helm of Radiance, Avenging Blade, Midgardian Mail, Bragi''s Harp, Damaru,
    Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.6
      win: 0.63
      pick: 0.26
      fit: 0.31
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.49
      fit: 0.37
    Stampede:
      total: 0.54
      efficiency: 0.52
      win: 0.71
      pick: 0.03
      fit: 0.24
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  - Freya's Tears
  - Shifter's Shield
  - Stampede
  flex_slots:
  - Stampede
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Amanita Charm, Jotunn''s
    Revenge, Kinetic Cuirass, Shield of the Phoenix, Berserker''s Shield, Hydra''s
    Lament, Soul Gem, Gluttonous Grimoire, Eye of Providence, Oni Hunter''s Garb,
    The Crusher, Chronos'' Pendant, Screeching Gargoyle, Chandra''s Grace, Spear of
    Desolation, Gladiator''s Shield, Spectral Armor, Erosion, Shield Splitter, Yogi''s
    Necklace, Pharaoh''s Curse, Prophetic Cloak, Draconic Scale, Helm of Radiance,
    Rod of Asclepius, Gem of Focus, Eye of the Storm, Arondight, Death Metal, Leviathan''s
    Hide, Jade Scepter, Midgardian Mail, Spear of the Magus, Mantle Of Discord, Hide
    of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.72
      win: 0.53
      pick: 0.27
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.58
      pick: 0.19
      fit: 0.48
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.6
      win: 0.63
      pick: 0.26
      fit: 0.32
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.61
      pick: 0.49
      fit: 0.45
    Stampede:
      total: 0.55
      efficiency: 0.52
      win: 0.71
      pick: 0.03
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Runeforged Hammer
  - Shifter's Shield
  - Stampede
  flex_slots:
  - Breastplate of Valor
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Berserker''s Shield, The Crusher, Jotunn''s
    Revenge, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence,
    Hydra''s Lament, Oni Hunter''s Garb, Shield Splitter, Freya''s Tears, Soul Gem,
    Golden Blade, Lernaean Bow, Eye of the Storm, Pharaoh''s Curse, Shield of the
    Phoenix, Death Metal, Spectral Armor, Avenging Blade, Erosion, Yogi''s Necklace,
    The Reaper, Damaru, Draconic Scale, Spear of the Magus, Shogun''s Ofuda, Leviathan''s
    Hide, Dominance, Heartseeker, The Cosmic Horror, Helm of Radiance, Rod of Asclepius,
    Riptalon, Midgardian Mail, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.27
      fit: 0.23
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.58
      pick: 0.19
      fit: 0.23
    Runeforged Hammer:
      total: 0.57
      efficiency: 0.6
      win: 0.63
      pick: 0.26
      fit: 0.44
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.49
      fit: 0.42
    Stampede:
      total: 0.54
      efficiency: 0.52
      win: 0.71
      pick: 0.03
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  - Gluttonous Grimoire
  - Shifter's Shield
  - Stampede
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Amanita Charm,
    The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Berserker''s Shield, Soul Gem,
    Eye of Providence, Oni Hunter''s Garb, Hydra''s Lament, Death Metal, Freya''s
    Tears, Spear of the Magus, Shield Splitter, The Cosmic Horror, Helm of Radiance,
    Shield of the Phoenix, Rod of Asclepius, Eye of the Storm, Spectral Armor, Erosion,
    Spear of Desolation, Jade Scepter, Yogi''s Necklace, Pharaoh''s Curse, Avenging
    Blade, Draconic Scale, Golden Blade, Obsidian Shard, Lernaean Bow, The Reaper,
    Triton''s Conch, Chronos'' Pendant, Damaru, Leviathan''s Hide, Wish-Granting Pearl.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.27
      fit: 0.23
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.58
      pick: 0.19
      fit: 0.23
    Runeforged Hammer:
      total: 0.57
      efficiency: 0.6
      win: 0.63
      pick: 0.26
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.49
      fit: 0.42
    Stampede:
      total: 0.54
      efficiency: 0.52
      win: 0.71
      pick: 0.03
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s
    Shield, Gluttonous Grimoire, Jotunn''s Revenge, Oni Hunter''s Garb, Freya''s Tears,
    The Crusher, Shield Splitter, Hydra''s Lament, Shield of the Phoenix, Eye of the
    Storm, Erosion, Draconic Scale, Spectral Armor, Pharaoh''s Curse, Soul Gem, Avenging
    Blade, Golden Blade, Yogi''s Necklace, Leviathan''s Hide, Death Metal, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Hide of the Nemean Lion, Lernaean Bow,
    Helm of Radiance, Damaru, Rod of Asclepius, Shogun''s Ofuda, Stampede, Magi''s
    Cloak, Ancile, Wyrmskin Hide.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.57
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.27
      fit: 0.31
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
---
