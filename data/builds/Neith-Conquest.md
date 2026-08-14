---
type: smite-build
god: Neith
mode: Conquest
builds:
- source: community
  aspect: Aspect of Wind
  aspect_pick_rate: 0.45
  aspect_win_rate: 0.5
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.27
    win_rate: 0.37
    alternates:
    - name: Tyrfing
      pick_rate: 0.22
      win_rate: 0.47
    - name: Book of Thoth
      pick_rate: 0.13
      win_rate: 0.48
  - name: The World Stone
    pick_rate: 0.14
    win_rate: 0.32
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.12
      win_rate: 0.54
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.48
  - name: Silverbranch Bow
    pick_rate: 0.11
    win_rate: 0.54
    alternates:
    - name: Soul Gem
      pick_rate: 0.1
      win_rate: 0.41
    - name: The World Stone
      pick_rate: 0.09
      win_rate: 0.33
  - name: Rod of Tahuti
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.11
      win_rate: 0.52
    - name: Obsidian Shard
      pick_rate: 0.11
      win_rate: 0.32
  - name: Obsidian Shard
    pick_rate: 0.12
    win_rate: 0.36
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.17
    - name: Silverbranch Bow
      pick_rate: 0.08
      win_rate: 0.5
  - name: Evil Eye
    pick_rate: 0.07
    win_rate: 0.38
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.07
      win_rate: 0.5
    - name: Manchu Bow
      pick_rate: 0.07
      win_rate: 0.75
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.16
    win_rate: 0.53
  - name: Archmage's Gem
    pick_rate: 0.15
    win_rate: 0.41
  - name: Conduit Gem
    pick_rate: 0.13
    win_rate: 0.41
  source_url: https://smitebrain.com/gods/neith/
  last_verified: '2026-08-14'
  god_win_rate: 0.4474885844748858
  god_matches_won: 98
  god_matches_played: 219
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Death Metal
  - Berserker's Shield
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
    this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Death Metal, Berserker''s
    Shield, Riptalon, Genji''s Guard, Spear of the Magus, Lernaean Bow, Damaru, Bracer
    of The Abyss, The Cosmic Horror, Hydra''s Lament, Breastplate of Valor, Bragi''s
    Harp, Blood-Bound Book, Golden Blade, Bancroft''s Talon, Nimble Ring, The Reaper,
    Chronos'' Pendant, Pharaoh''s Curse, Tekko-Kagi, Runeforged Hammer, Dominance,
    Helm of Radiance, Kinetic Cuirass, Rod of Asclepius, Amanita Charm, Oni Hunter''s
    Garb, Freya''s Tears, Jade Scepter, Doom Orb, Eye of Providence.'
  slot_scores:
    Berserker's Shield:
      total: 0.48
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.49
      efficiency: 0.58
      win: 0.47
      pick: 0.0
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.48
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.54
      win: 0.54
      pick: 0.17
      fit: 0.35
    The Crusher:
      total: 0.49
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.38
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Silverbranch Bow
  - Damaru
  - Demon Blade
  flex_slots:
  - Damaru
  - Demon Blade
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
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Jotunn''s Revenge, Death Metal, The Crusher, Berserker''s
    Shield, Genji''s Guard, Riptalon, Damaru, Spear of the Magus, Lernaean Bow, The
    Cosmic Horror, Hydra''s Lament, Bracer of The Abyss, Breastplate of Valor, Blood-Bound
    Book, Bragi''s Harp, Bancroft''s Talon, Golden Blade, The Reaper, Nimble Ring,
    Chronos'' Pendant, Pharaoh''s Curse, Runeforged Hammer, Helm of Radiance, Tekko-Kagi,
    Kinetic Cuirass, Dominance, Amanita Charm, Rod of Asclepius, Oni Hunter''s Garb,
    Freya''s Tears, Jade Scepter, Eye of Providence, Doom Orb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.35
    Death Metal:
      total: 0.49
      efficiency: 0.58
      win: 0.47
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.48
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.54
      win: 0.54
      pick: 0.17
      fit: 0.33
    Damaru:
      total: 0.47
      efficiency: 0.58
      win: 0.47
      pick: 0.0
      fit: 0.36
    Demon Blade:
      total: 0.43
      efficiency: 0.37
      win: 0.47
      pick: 0.0
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Death Metal
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
    god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Genji''s Guard, Death
    Metal, Berserker''s Shield, Riptalon, Spear of the Magus, Hydra''s Lament, The
    Cosmic Horror, Breastplate of Valor, Lernaean Bow, Damaru, Bracer of The Abyss,
    The Reaper, Chronos'' Pendant, Golden Blade, Blood-Bound Book, Bragi''s Harp,
    Bancroft''s Talon, Tekko-Kagi, Runeforged Hammer, Pharaoh''s Curse, Nimble Ring,
    Freya''s Tears, Kinetic Cuirass, Helm of Radiance, Dominance, Heartseeker, Amanita
    Charm, Doom Orb, Oni Hunter''s Garb, Shield of the Phoenix, Dreamer''s Idol.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.71
      win: 0.47
      pick: 0.0
      fit: 0.13
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.46
    Death Metal:
      total: 0.48
      efficiency: 0.58
      win: 0.47
      pick: 0.0
      fit: 0.43
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.49
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.54
      win: 0.54
      pick: 0.17
      fit: 0.37
    The Crusher:
      total: 0.5
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
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
    of the Phoenix, Rod of Asclepius, Blood-Bound Book, Bancroft''s Talon, Genji''s
    Guard, Jotunn''s Revenge, Kinetic Cuirass, The Crusher, The Reaper, Death Metal,
    Chandra''s Grace, Breastplate of Valor, Pharaoh''s Curse, Oni Hunter''s Garb,
    Spear of the Magus, Freya''s Tears, Golden Blade, Lifebinder, Hydra''s Lament,
    Lernaean Bow, Damaru, Runeforged Hammer, The Cosmic Horror, Phoenix Feather, Shogun''s
    Ofuda, Bracer of The Abyss, Spectral Armor, Helm of Radiance, Umbral Link, Jade
    Scepter, Shifter''s Shield, Erosion, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.71
      win: 0.47
      pick: 0.0
      fit: 0.15
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.59
      win: 0.47
      pick: 0.0
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.52
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Silverbranch Bow
  - Spear of the Magus
  - The Crusher
  flex_slots:
  - Spear of the Magus
  - Berserker's Shield
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Riptalon, Spear
    of the Magus, Berserker''s Shield, The Cosmic Horror, Death Metal, Genji''s Guard,
    The Reaper, Lernaean Bow, Damaru, Hydra''s Lament, Avenging Blade, Bracer of The
    Abyss, Screeching Gargoyle, Breastplate of Valor, Tekko-Kagi, Blood-Bound Book,
    Bancroft''s Talon, Golden Blade, Doom Orb, Bragi''s Harp, Dreamer''s Idol, Heartseeker,
    Stone of Binding, Nimble Ring, Pharaoh''s Curse, Chronos'' Pendant, Runeforged
    Hammer, Kinetic Cuirass, Helm of Radiance, Void Shield, Amanita Charm, Dominance.'
  slot_scores:
    Berserker's Shield:
      total: 0.48
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.17
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.57
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.54
      win: 0.54
      pick: 0.17
      fit: 0.44
    Spear of the Magus:
      total: 0.48
      efficiency: 0.6
      win: 0.47
      pick: 0.0
      fit: 0.4
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - The Crusher
  - Berserker's Shield
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Jotunn''s Revenge, Riptalon, The Crusher, Berserker''s
    Shield, Death Metal, Genji''s Guard, Golden Blade, Lernaean Bow, Spear of the
    Magus, Bracer of The Abyss, Damaru, Hydra''s Lament, The Cosmic Horror, Breastplate
    of Valor, Bragi''s Harp, Blood-Bound Book, Bancroft''s Talon, Pharaoh''s Curse,
    Nimble Ring, The Reaper, Chronos'' Pendant, Runeforged Hammer, Kinetic Cuirass,
    Dominance, Helm of Radiance, Amanita Charm, Tekko-Kagi, Oni Hunter''s Garb, Rod
    of Asclepius, Freya''s Tears, Eye of Providence, Toxic Blade, Jade Scepter, Shogun''s
    Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.48
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.3
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.42
    Riptalon:
      total: 0.49
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.52
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.54
      win: 0.54
      pick: 0.17
      fit: 0.46
    The Crusher:
      total: 0.48
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Hydra's Lament
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
    Gluttonous Grimoire, Breastplate of Valor, Hydra''s Lament, The Crusher, Berserker''s
    Shield, Death Metal, Riptalon, Chronos'' Pendant, Freya''s Tears, Lernaean Bow,
    Spear of the Magus, Damaru, Shield of the Phoenix, The Cosmic Horror, Bracer of
    The Abyss, Gem of Focus, Golden Blade, Screeching Gargoyle, Pharaoh''s Curse,
    Blood-Bound Book, Bancroft''s Talon, Chandra''s Grace, The Reaper, Kinetic Cuirass,
    Amanita Charm, Nimble Ring, Bragi''s Harp, Runeforged Hammer, Arondight, Oni Hunter''s
    Garb, Pendulum Blade, Eye of Providence, Dominance, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.71
      win: 0.47
      pick: 0.0
      fit: 0.28
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.49
    Hydra's Lament:
      total: 0.48
      efficiency: 0.58
      win: 0.47
      pick: 0.0
      fit: 0.46
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.54
      win: 0.54
      pick: 0.17
      fit: 0.31
    Soul Gem:
      total: 0.5
      efficiency: 0.59
      win: 0.41
      pick: 0.16
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - The Crusher
  - Berserker's Shield
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    Death Metal, The Crusher, Berserker''s Shield, Genji''s Guard, Spear of the Magus,
    The Cosmic Horror, Bracer of The Abyss, Riptalon, Hydra''s Lament, Breastplate
    of Valor, Lernaean Bow, Damaru, Blood-Bound Book, Bancroft''s Talon, Bragi''s
    Harp, Chronos'' Pendant, Nimble Ring, Helm of Radiance, Golden Blade, The Reaper,
    Rod of Asclepius, Pharaoh''s Curse, Jade Scepter, Runeforged Hammer, Gem of Focus,
    Doom Orb, Kinetic Cuirass, Freya''s Tears, Tekko-Kagi, Amanita Charm, Dreamer''s
    Idol, Dominance, Ancient Signet.'
  slot_scores:
    Berserker's Shield:
      total: 0.48
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.49
      efficiency: 0.58
      win: 0.47
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.52
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.54
      win: 0.54
      pick: 0.17
      fit: 0.32
    The Crusher:
      total: 0.49
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Silverbranch Bow
  - Berserker's Shield
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    The Crusher, Death Metal, Berserker''s Shield, Genji''s Guard, Spear of the Magus,
    Lernaean Bow, Riptalon, Damaru, Hydra''s Lament, The Cosmic Horror, Bracer of
    The Abyss, Bragi''s Harp, Breastplate of Valor, Golden Blade, Blood-Bound Book,
    Bancroft''s Talon, The Reaper, Nimble Ring, Runeforged Hammer, Chronos'' Pendant,
    Tekko-Kagi, Dominance, Pharaoh''s Curse, Helm of Radiance, Rod of Asclepius, Kinetic
    Cuirass, Amanita Charm, Jade Scepter, Oni Hunter''s Garb, Heartseeker, Doom Orb,
    Freya''s Tears.'
  slot_scores:
    Berserker's Shield:
      total: 0.48
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.49
      efficiency: 0.58
      win: 0.47
      pick: 0.0
      fit: 0.53
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.48
    Silverbranch Bow:
      total: 0.49
      efficiency: 0.54
      win: 0.54
      pick: 0.17
      fit: 0.33
    The Crusher:
      total: 0.5
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Soul Gem
  flex_slots:
  - Death Metal
  - Berserker's Shield
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
    Death Metal, Berserker''s Shield, Riptalon, Genji''s Guard, Spear of the Magus,
    Lernaean Bow, Damaru, Bracer of The Abyss, The Cosmic Horror, Hydra''s Lament,
    Breastplate of Valor, Bragi''s Harp, Blood-Bound Book, Golden Blade, Bancroft''s
    Talon, Nimble Ring, The Reaper, Chronos'' Pendant, Pharaoh''s Curse, Tekko-Kagi,
    Runeforged Hammer, Dominance, Helm of Radiance, Kinetic Cuirass, Rod of Asclepius,
    Amanita Charm, Oni Hunter''s Garb, Freya''s Tears, Jade Scepter, Doom Orb, Eye
    of Providence.'
  slot_scores:
    Berserker's Shield:
      total: 0.48
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.49
      efficiency: 0.58
      win: 0.47
      pick: 0.0
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.47
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.49
      efficiency: 0.63
      win: 0.47
      pick: 0.0
      fit: 0.38
    Soul Gem:
      total: 0.48
      efficiency: 0.59
      win: 0.41
      pick: 0.16
      fit: 0.56
  starter: *id001
---
